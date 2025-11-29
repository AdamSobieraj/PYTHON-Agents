from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct
import numpy as np
from openai import OpenAI

class SearchKnowledgebase:
    def __init__(self, client: OpenAI, knowledge_path: str,
                 qdrant_client: QdrantClient, collection_name: str,
                 embedding_model="text-embedding-3-small"):
        self.client = client
        self.model = embedding_model
        self.knowledge_path = knowledge_path
        self.qdrant = qdrant_client
        self.collection_name = collection_name

        self.knowledgebase = self._load_knowledgebase(knowledge_path)

        # Utworzenie kolekcji jeśli nie istnieje
        existing = [c.name for c in self.qdrant.get_collections().collections]
        if self.collection_name not in existing:
            self.qdrant.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=1536, distance="Cosine")
            )

        self._upload_embeddings_to_qdrant()

    def _load_knowledgebase(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Plik {path} nie znaleziony!")
            return []

    def _get_embedding(self, text: str):
        text = text.replace("\n", " ")
        emb = self.client.embeddings.create(input=[text], model=self.model)
        return np.array(emb.data[0].embedding, dtype=np.float32)

    def _upload_embeddings_to_qdrant(self):
        points = []
        for idx, text in enumerate(self.knowledgebase):
            emb = self._get_embedding(text)
            points.append(PointStruct(id=idx, vector=emb.tolist(), payload={"text": text}))

        if points:
            self.qdrant.upsert(
                collection_name=self.collection_name,
                points=points
            )

    def search(self, query: str, top_x=3):
        query_vec = self._get_embedding(query).tolist()

        response = self.qdrant.query_points(
            collection_name=self.collection_name,
            query=query_vec,
            limit=top_x,
            with_payload=True
        )

        # Sprawdź, gdzie są punkty
        if hasattr(response, "points"):
            results = response.points
        elif hasattr(response, "result"):
            results = response.result
        else:
            # fallback, traktujemy response jako listę
            results = list(response)

        texts = []
        for point in results:
            # punkt może być dict lub PointStruct
            if isinstance(point, dict):
                texts.append(point.get("payload", {}).get("text", str(point)))
            else:
                texts.append(str(point))

        return texts

