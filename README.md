# 📘 AI Handbook Generator (LightRAG + LongWriter)

An end-to-end AI engineering project that generates long-form handbooks (20,000+ words) from PDF documents using Retrieval-Augmented Generation (RAG), LightRAG-compatible architecture, Supabase vector storage, and a Hugging Face LLM.

This project was built as part of an AI Engineering assignment and focuses on system design, modularity, and long-form generation pipelines rather than model fine-tuning.

---

## 🚀 Key Features

- 📄 PDF upload and text extraction
- ✂️ Chunking and semantic indexing
- 🧠 LightRAG-style retrieval using Supabase + pgvector
- 🤖 Hugging Face LLM  for section writing
- 📝 LongWriter-style iterative handbook generation
- 📘 20,000+ word handbook generation
- 💬 Chat-based RAG interface (Streamlit)
- ⬇️ Exportable handbook (Markdown)

---

## 🏗️ System Architecture

PDF Upload
↓
Text Extraction (pdfplumber)
↓
Chunking
↓
Sentence-BERT Embeddings
↓
Supabase Vector DB (pgvector)
↓
LightRAG Retrieval
↓
Hugging Face LLM (FLAN-T5)
↓
LongWriter-style Iterative Loop
↓
20,000+ Word Handbook



The retrieval and generation layers are fully decoupled, allowing easy replacement of models or vector stores.

---

## 🧠 Retrieval-Augmented Generation (RAG)

- Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
- Vector store: Supabase PostgreSQL with `pgvector`
- Similarity search: cosine distance via SQL RPC
- Retrieval strategy: top-k semantic search

All generated content is grounded strictly in retrieved document context.

---

## ✍️ LongWriter-Style Handbook Generation

The handbook generator follows a LongWriter-style architecture:

- Topic-based outline generation
- Section-by-section writing
- Iterative loop until target word count (20,000 words)
- Each section retrieves fresh context via LightRAG
- Hugging Face LLM rewrites retrieved context into coherent text

This design supports scalable long-form generation without relying on a single prompt.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **UI:** Streamlit
- **PDF Processing:** pdfplumber
- **Embeddings:** Sentence-BERT
- **Vector DB:** Supabase + pgvector
- **LLM:** Hugging Face FLAN-T5 (local inference)
- **Environment:** python-dotenv

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

streamlit run app.py
python test_handbook.py

