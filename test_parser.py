from pdf_processing.parser import extract_text_from_pdf
text = extract_text_from_pdf("RNA.pdf")
print(text[:1000])

