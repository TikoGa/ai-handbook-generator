import os
import requests


class GrokWriter:
    def __init__(self):
        self.api_key = os.getenv("GROK_API_KEY")
        self.api_url = "https://api.x.ai/v1/chat/completions"

    def write_section(self, title: str, context: str, question: str = None) -> str:
        """
        Generates a grounded, human-readable answer using Grok.
        The model is allowed to rephrase and summarize, but NOT to add new facts.
        """

        if not self.api_key:
            return "GROK_API_KEY is not set."

        if question:
            user_query = question
        else:
            user_query = title

        prompt = (
            "You are a document-grounded assistant.\n\n"
            "Answer the question using ONLY the information from the context below.\n"
            "You MAY rephrase and summarize the information for clarity,\n"
            "but you MUST NOT add any new facts or external knowledge.\n\n"
            "If the answer is not present in the context, respond exactly with:\n"
            "\"The uploaded document does not contain this information.\"\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{user_query}\n\n"
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
