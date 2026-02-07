from supabase import create_client
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()


class LightRAGStore:
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_SERVICE_KEY")
        self.supabase = create_client(url, key)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_texts(self, texts):
        for text in texts:
            embedding = self.model.encode(text).tolist()
            self.supabase.table("documents").insert({
                "content": text,
                "embedding": embedding
            }).execute()

    def search(self, query, top_k=3):
        query_embedding = self.model.encode(query).tolist()
        response = self.supabase.rpc(
            "match_documents",
            {
                "query_embedding": query_embedding,
                "match_count": top_k
            }
        ).execute()

        return [row["content"] for row in response.data]

    def clear(self):
        self.supabase.table("documents").delete().neq("content", "").execute()
