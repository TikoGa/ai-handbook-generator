# AI Handbook Generator (RAG-based PDF QA)

This project implements a Retrieval-Augmented Generation (RAG) system that allows users to upload a PDF document and ask natural language questions about its content. The system retrieves relevant passages from the document and generates grounded, human-readable answers using a large language model.

The focus of this project is correctness, grounding, and robustness rather than UI complexity.

---

## ✨ Features

- PDF upload and text extraction
- Text chunking and vector embedding
- Vector storage using Supabase
- Semantic retrieval (LightRAG-style)
- Grounded answer generation using a free LLM via OpenRouter
- Protection against hallucination by restricting answers to document context
- Automatic clearing of old document embeddings on new upload

---

## 🧠 Architecture Overview

1. **PDF Parsing**
   - Extracts raw text from uploaded PDF files.

2. **Chunking**
   - Splits the text into overlapping chunks suitable for semantic search.

3. **Vector Store (Supabase)**
   - Each chunk is embedded using a sentence-transformer model.
   - Embeddings are stored in Supabase for similarity search.

4. **Retrieval**
   - For each user query, the most relevant chunks are retrieved using vector similarity.

5. **Answer Generation**
   - Retrieved chunks are passed to an LLM with a strict prompt.
   - The model may rephrase or summarize but is not allowed to add external information.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Vector Database**: Supabase (PostgreSQL + pgvector)
- **Embeddings**: sentence-transformers (MiniLM)
- **LLM Provider**: OpenRouter (free models)
- **Language**: Python

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt


SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_supabase_service_key
OPENROUTER_API_KEY=your_openrouter_key



streamlit run app.py

