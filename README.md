# 📘 AI Handbook Generator (Local RAG)

An AI-powered chat application that allows users to upload PDF documents, ask questions about their content, and receive grounded, context-aware answers using a local Retrieval-Augmented Generation (RAG) pipeline.

This project demonstrates practical AI engineering skills in document ingestion, semantic retrieval, and system design.

---

## 🚀 Features

- 📄 **PDF Upload** – Upload text-based PDF documents
- ✂️ **Text Extraction & Chunking** – Parse and split documents into overlapping chunks
- 🧠 **Semantic Retrieval (Local RAG)** – Sentence-BERT embeddings with cosine similarity
- 💬 **Chat Interface** – Ask questions grounded strictly in the uploaded document
- 🧩 **Modular Generation Layer** – Can be plugged into any instruction-tuned LLM

---

## 🏗️ System Architecture


PDF Upload
↓
Text Extraction (pdfplumber)
↓
Text Chunking
↓
Sentence-BERT Embeddings
↓
Local Semantic Search (Cosine Similarity)
↓
Chat Interface (Streamlit)
↓
Grounded Answer


The system is designed to be explainable and deterministic, avoiding hallucinations by grounding all responses in retrieved document content.

---

## 🧠 Retrieval-Augmented Generation (RAG)

- Embeddings are generated locally using:
  - `sentence-transformers/all-MiniLM-L6-v2`
- No external vector database is used
- Semantic search is performed using cosine similarity
- Only the top-k most relevant chunks are used to answer a query

This approach ensures:
- Full reproducibility
- No dependency on external infrastructure
- Clear separation between retrieval and generation layers

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **UI:** Streamlit
- **PDF Processing:** pdfplumber
- **Embeddings:** Sentence-BERT (sentence-transformers)
- **Retrieval:** Local cosine similarity search
- **Environment Management:** python-dotenv

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-handbook-generator
2. Install dependencies
pip install -r requirements.txt

3. (Optional) Create .env

If you plan to connect an external LLM later:

OPENAI_API_KEY=your_key_here

4. Run the application
streamlit run app.py

🧪 Example Usage

Upload a PDF (e.g., a research paper)

Ask a question such as:

“What models are discussed in file?”

Receive a response grounded strictly in the uploaded documet
