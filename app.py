import streamlit as st

from pdf_processing.parser import extract_text_from_pdf
from rag.chunker import chunk_text

from rag.vectorstore import LightRAGStore
from rag.llm_writer import OpenRouterWriter


st.set_page_config(page_title="PDF RAG Chat", layout="centered")

st.title("📄 PDF Question Answering with RAG")


# -----------------------------
# PDF Upload & Indexing
# -----------------------------
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Save uploaded PDF temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract and chunk text
    text = extract_text_from_pdf("temp.pdf")
    chunks = chunk_text(text)

    # Initialize vector store
    store = LightRAGStore()

    # 🔥 Clear previous document chunks
    store.clear()

    # ➕ Add only current PDF chunks
    store.add_texts(chunks)

    # Save store in session
    st.session_state.store = store

    st.success(f"PDF indexed successfully ({len(chunks)} chunks)")


# -----------------------------
# Question Answering
# -----------------------------
st.markdown("---")
question = st.text_input("Ask a question about the document")

if question:
    if "store" not in st.session_state:
        st.warning("Please upload a PDF first.")
    else:
        store = st.session_state.store

        # 🔍 Retrieve relevant chunks
        results = store.search(question, top_k=3)

        if not results:
            st.write("The uploaded document does not contain this information.")
        else:
            retrieved_context = "\n\n".join(results)

            writer = OpenRouterWriter()
            answer = writer.write_section(
                title="Question",
                context=retrieved_context,
                question=question
            )

            st.markdown("### 💬 Answer")
            st.write(answer)
