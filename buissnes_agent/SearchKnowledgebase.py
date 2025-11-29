import numpy as np
import pandas as pd
from openai import OpenAI
from scipy.spatial.distance import cosine, euclidean


class SearchKnowledgebase:
    def __init__(self, client: OpenAI, knowledgebase: list, model="text-embedding-3-large"):
        self.client = client
        self.model = model
        self.knowledgebase = knowledgebase

        # Tworzymy embeddingi przy starcie
        print("Generuję embeddingi dla bazy wiedzy...")
        self.df = self._build_database()
        print("Baza wiedzy gotowa.\n")

    def get_embedding(self, text: str):
        text = text.replace("\n", " ")
        emb = self.client.embeddings.create(
            model=self.model,
            input=[text]
        )
        return emb.data[0].embedding

    def robust_norm(self, x):
        x = np.array(x, dtype=float)
        if not np.isfinite(x).all():
            return None
        if np.all(x == 0):
            return 0.0

        max_val = np.max(np.abs(x))
        if max_val == 0:
            return 0.0

        scaled = x / max_val
        norm_scaled = np.sqrt(np.sum(scaled**2))
        return norm_scaled * max_val

    def safe_vector(self, u, eps=1e-12, clip_value=1e100):
        u = np.array(u, dtype=np.float64)
        if not np.isfinite(u).all():
            return None

        norm = np.linalg.norm(u)
        if norm < eps:
            return None

        u = np.clip(u, -clip_value, clip_value)
        u = u / norm
        return u

    def safe_cosine(self, u, v):
        u_s = self.safe_vector(u)
        v_s = self.safe_vector(v)
        if u_s is None or v_s is None:
            return np.nan
        return cosine(u_s, v_s)

    def safe_euclidean(self, u, v):
        u_s = self.safe_vector(u)
        v_s = self.safe_vector(v)
        if u_s is None or v_s is None:
            return np.nan
        return euclidean(u_s, v_s)

    def _build_database(self):
        embeddings = [self.get_embedding(text) for text in self.knowledgebase]

        cleaned_records = []
        for text, vec in zip(self.knowledgebase, embeddings):
            n = self.robust_norm(vec)
            vec = vec / n
            cleaned_records.append((text, vec))

        return pd.DataFrame(cleaned_records, columns=["Text", "Vector"])

    def search(self, query, top_x=5, distance="cosine"):

        query_vector = self.get_embedding(query)

        if distance == "cosine":
            self.df["Distance"] = self.df["Vector"].apply(
                lambda v: self.safe_cosine(v, query_vector)
            )
        else:
            self.df["Distance"] = self.df["Vector"].apply(
                lambda v: self.safe_euclidean(v, query_vector)
            )

        return self.df.nsmallest(top_x, "Distance")
