import os
import requests
from dotenv import load_dotenv

load_dotenv()


class OpenRouterWriter:
    """
    OpenRouter-based LLM writer (FREE models).
    Uses DeepSeek Chat for grounded answer generation.
    """

    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

    def write_section(self, title: str, context: str, question: str = None) -> str:
        if not self.api_key:
            return "OPENROUTER_API_KEY is not set."

        if not context.strip():
            return "The uploaded document does not contain this information."

        user_query = question if question else title

        prompt = (
                  "You are a document-grounded assistant.\n"
                  "Answer the question using ONLY the information from the context below.\n"
                  "You MAY rephrase and summarize the information for clarity,\n"
                  "but you MUST NOT add any new facts or external knowledge.\n\n"
                  "IMPORTANT RULES:\n"
                  "- Do NOT return JSON\n"
                  "- Do NOT include IDs, categories, or metadata\n"
                  "- Do NOT explain how you derived the answer\n"
                  "- Return ONLY a direct, natural-language answer to the question\n\n"
                  f"Context:\n{context}\n\n"
                  f"Question:\n{user_query}\n\n"
                  "Answer (plain text only):"
                  ) 

        response = requests.post(
            self.api_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "ai-handbook-generator",
            },
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.2,
            },
            timeout=60,
        )

        if response.status_code != 200:
            return f"OpenRouter API error: {response.text}"

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
