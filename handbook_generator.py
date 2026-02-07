from rag.vectorstore import LightRAGStore
from rag.llm_writer import HFWriter

TARGET_WORDS = 2000


class HandbookGenerator:
    def __init__(self):
        self.store = LightRAGStore()
        self.writer = HFWriter()
        self.handbook = ""

    def generate_outline(self, topic: str):
        return [
            f"Introduction to {topic}",
            f"Biological background of {topic}",
            "Classical computational models",
            "Thermodynamic and MFE-based approaches",
            "Comparative sequence analysis",
            "Machine learning methods",
            "Deep learning approaches",
            "Evaluation metrics and benchmarks",
            "Challenges and limitations",
            "Future directions",
        ]

    def generate_section(self, section_title: str):
        query = f"{section_title} detailed explanation"
        context_chunks = self.store.search(query, top_k=5)
        context = " ".join(context_chunks)

        section_text = f"\n\n## {section_title}\n\n"
        section_text += self.writer.write_section(section_title, context)

        return section_text

    def generate_handbook(self, topic: str):
        outline = self.generate_outline(topic)
        section_index = 0

        while self.word_count() < TARGET_WORDS:
            section_title = outline[section_index % len(outline)]
            part = section_index // len(outline) + 1
            full_title = f"{section_title} (Part {part})"

            section_text = self.generate_section(full_title)
            self.handbook += section_text

            section_index += 1

        return self.handbook

    def word_count(self):
        return len(self.handbook.split())
