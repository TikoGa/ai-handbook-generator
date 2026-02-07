import os
from supabase import create_client
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import numpy as np

load_dotenv()

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)


class LightRAGStore:
    def add_texts(self, texts):
        for text in texts:
            embedding = model.encode(text).tolist()
            supabase.table("documents").insert({
                "content": text,
                "embedding": embedding
            }).execute()

    def search(self, query, top_k=3):
        query_embedding = model.encode(query).tolist()

        result = supabase.rpc(
            "match_documents",
            {
                "query_embedding": query_embedding,
                "match_count": top_k
            }
        ).execute()

        return [row["content"] for row in result.data]
