import numpy as np
from sentence_transformers import SentenceTransformer

class LocalEmbeddingStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.embeddings = []
        self.texts = []

    def add_texts(self, chunks: list[str]):
        for chunk in chunks:
            emb = self.model.encode(chunk)
            self.embeddings.append(emb)
            self.texts.append(chunk)

        self.embeddings = np.array(self.embeddings)

    def search(self, query: str, top_k: int = 5):
        query_emb = self.model.encode(query)

        # cosine similarity
        scores = self.embeddings @ query_emb / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_emb)
        )

        top_indices = scores.argsort()[-top_k:][::-1]

        return [self.texts[i] for i in top_indices]
