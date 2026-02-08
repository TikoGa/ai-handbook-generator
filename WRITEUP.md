```markdown
# Technical Writeup: RAG-Based PDF Question Answering System

## 1. Problem Statement

Large Language Models (LLMs) are powerful but prone to hallucination when answering questions about specific documents. The goal of this project is to build a system that ensures answers are strictly grounded in the content of a user-provided PDF document while still being human-readable and natural.

---

## 2. System Design

The system follows the Retrieval-Augmented Generation (RAG) paradigm:

1. Retrieve relevant document fragments.
2. Generate answers using an LLM constrained by the retrieved context.

This separation ensures factual grounding while maintaining flexibility in language generation.

---

## 3. PDF Processing and Chunking

After upload, the PDF is parsed into raw text.  
The text is split into overlapping chunks to preserve semantic continuity across chunk boundaries.

Chunking allows:
- Efficient vector embedding
- Scalable retrieval
- Better semantic matching for long documents

---

## 4. Vector Storage and Retrieval

Each chunk is embedded using a sentence-transformer model and stored in a Supabase-backed vector database.

### Key design decision:
On every new PDF upload, all previous embeddings are deleted.

**Reason:**  
This prevents retrieval of content from previously uploaded documents and guarantees that all answers refer only to the currently active document.

---

## 5. Retrieval Strategy

For each user query:
- The query is embedded.
- The top-k most similar chunks are retrieved using vector similarity.

This ensures that the LLM only sees the most relevant parts of the document.

---

## 6. Answer Generation and Prompt Design

The LLM is not allowed to answer freely.

The prompt explicitly enforces:
- Use only the provided context
- No external knowledge
- No hallucination
- No structured or dataset-style outputs (e.g., JSON, metadata)

The model is allowed to:
- Rephrase
- Summarize
- Produce natural language answers

This results in **abstractive but grounded** responses.

---

## 7. Model Choice and Adaptability

Initially, Grok was considered for long-context generation. However, due to licensing constraints, the system was adapted to use free LLMs via OpenRouter.

This demonstrates an important engineering principle:
> The RAG architecture is model-agnostic.

Changing the LLM provider does not affect:
- Retrieval logic
- Vector storage
- Grounding guarantees

---

## 8. Error Handling and Robustness

The system explicitly handles:
- Empty retrieval results
- Missing information in the document
- API permission or availability issues

In such cases, the user is informed clearly rather than receiving an incorrect answer.

---

## 9. Key Engineering Insights

- Retrieval quality matters more than model size.
- Prompt constraints are essential to avoid hallucination.
- Clearing the vector store on document change is critical in single-document QA systems.
- LLM providers can be swapped without changing core architecture.

---

## 10. Conclusion

This project demonstrates a complete, robust RAG pipeline for document-based question answering. It prioritizes correctness, grounding, and adaptability over superficial complexity, aligning closely with real-world AI engineering practices.
