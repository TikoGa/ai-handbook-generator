from pdf_processing.parser import extract_text_from_pdf
from rag.chunker import chunk_text

text = extract_text_from_pdf("RNA.pdf")
chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")
print(chunks[0][:500])
