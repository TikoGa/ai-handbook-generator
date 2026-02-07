import streamlit as st

from pdf_processing.parser import extract_text_from_pdf
from rag.chunker import chunk_text
from rag.embeddings import LocalEmbeddingStore

st.set_page_config(page_title="AI Handbook Generator", layout="wide")

st.title("📘 AI Handbook Generator (Local RAG)")

# Session state
if "store" not in st.session_state:
    st.session_state.store = None

# PDF upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf("temp.pdf")
    chunks = chunk_text(text)

    store = LocalEmbeddingStore()
    store.add_texts(chunks)

    st.session_state.store = store

    st.success(f"PDF indexed successfully ({len(chunks)} chunks)")

# Chat input
query = st.text_input("Ask a question about the document")

if query and st.session_state.store:
    results = st.session_state.store.search(query, top_k=3)

    st.subheader("📌 Retrieved context")
    for i, r in enumerate(results, 1):
        st.markdown(f"**Chunk {i}:**")
        st.write(r[:800])
        st.markdown("---")

