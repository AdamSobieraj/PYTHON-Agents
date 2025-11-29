import numpy as np
import pandas as pd
from openai import OpenAI
from scipy.spatial.distance import cosine

class SearchKnowledgebase:
    def __init__(self, client: OpenAI, knowledge_path: str, embedding_model="text-embedding-3-large"):
        self.client = client
        self.model = embedding_model
        self.knowledge_path = knowledge_path

        self.knowledgebase = self._load_knowledgebase(knowledge_path)

        self.df = self._build_embeddings(self.knowledgebase)

    def _load_knowledgebase(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
            return lines
        except FileNotFoundError:
            print(f" Plik {path} nie znaleziony!")
            return []

    def _get_embedding(self, text: str):
        text = text.replace("\n", " ")
        emb = self.client.embeddings.create(input=[text], model=self.model)
        return np.array(emb.data[0].embedding, dtype=np.float32)

    def _build_embeddings(self, knowledgebase):
        records = []
        for text in knowledgebase:
            emb = self._get_embedding(text)
            records.append((text, emb))
        return pd.DataFrame(records, columns=["Text", "Vector"])

    def _safe_cosine(self, u, v):
        if u is None or v is None:
            return np.nan
        try:
            u_norm = u / np.linalg.norm(u)
            v_norm = v / np.linalg.norm(v)
            return cosine(u_norm, v_norm)
        except:
            return np.nan

    def search(self, query: str, top_x=3):
        query_vec = self._get_embedding(query)
        self.df["Distance"] = self.df["Vector"].apply(lambda x: self._safe_cosine(x, query_vec))
        return self.df.nsmallest(top_x, "Distance")
