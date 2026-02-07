import os
import requests


class GrokWriter:
    def __init__(self):
        self.api_key = os.getenv("GROK_API_KEY")
        self.api_url = "https://api.x.ai/v1/chat/completions"

    def write_section(self, title: str, context: str) -> str:
        if not self.api_key:
            return "GROK_API_KEY is not set."

        prompt = (
            "You are a document-grounded assistant.\n\n"
            "Write a section using ONLY the information in the context.\n"
            "Do NOT add external knowledge.\n"
            "If the context does not contain enough information, say so.\n\n"
            f"Section title:\n{title}\n\n"
            f"Context:\n{context}\n\n"
            "Answer:\n"
        )

        response = requests.post(
            self.api_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "grok-4.1",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.2,
            },
            timeout=60,
        )

        if response.status_code != 200:
            return f"Grok API error: {response.text}"

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
