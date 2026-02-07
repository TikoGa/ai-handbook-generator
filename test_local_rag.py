from pdf_processing.parser import extract_text_from_pdf
from rag.chunker import chunk_text
from rag.embeddings import LocalEmbeddingStore

text = extract_text_from_pdf("RNA.pdf")
chunks = chunk_text(text)

store = LocalEmbeddingStore()
store.add_texts(chunks)

results = store.search(
    "What is RNA secondary structure prediction?",
    top_k=2
)

print("Top results:\n")
for r in results:
    print(r[:500])
    print("-" * 50)

