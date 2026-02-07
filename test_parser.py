from pdf_processing.parser import extract_text_from_pdf
text = extract_text_from_pdf("RAG.pdf")
print(text[:1000])

