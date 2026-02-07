import streamlit as st
from rag.generator import generate_answer
from pdf_processing.parser import extract_text_from_pdf
from rag.chunker import chunk_text
from rag.vectorstore import LightRAGStore
from handbook_generator import HandbookGenerator


st.set_page_config(page_title="AI Handbook Generator", layout="wide")

st.title("📘 AI Handbook Generator")
st.divider()
st.header("📘 Handbook Generator (LongWriter-style)")

topic = st.text_input(
    "Enter handbook topic",
    value="RNA secondary structure prediction"
)

if st.button("Generate handbook"):
    with st.spinner("Generating handbook... this may take a few minutes"):
        generator = HandbookGenerator()
        handbook_text = generator.generate_handbook(topic)

    st.success("Handbook generated!")

    st.download_button(
        label="⬇️ Download handbook (Markdown)",
        data=handbook_text,
        file_name="handbook.md",
        mime="text/markdown"
    )

    st.text_area(
        "Preview (first 2000 characters)",
        handbook_text[:2000],
        height=300
    )

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

    store = LightRAGStore()
    store.add_texts(chunks)

    st.session_state.store = store

    st.success(f"PDF indexed successfully ({len(chunks)} chunks)")

# Chat input
query = st.text_input("Ask a question about the document")

if query and st.session_state.store:
    results = st.session_state.store.search(query, top_k=3)

    context = "\n\n".join(results)

    answer = generate_answer(context, query)

    st.subheader("💬 Answer")
    st.write(answer)

