# 📨 Grievance Assistant Chatbot (RAG + OpenAI)

A smart chatbot that:
- Registers user complaints
- Retrieves status
- Uses RAG (PDF-based) context + OpenAI LLM

### 🚀 Features
- OpenAI (GPT-3.5) for conversation
- FAISS vector search from grievance_policy.pdf
- Streamlit frontend
- API integration for complaint registration/status

### 🧠 Powered By
- LangChain
- FAISS
- OpenAI GPT-3.5
- Streamlit

### 🛠️ To Run Locally

1. `pip install -r requirements.txt`
2. Create `.env` with your OpenAI key
3. `from rag_utils import create_vector_store_from_pdf; create_vector_store_from_pdf()`
4. `streamlit run app.py`

### 💬 Example Input

> I want to raise a complaint about my broken laptop.

---

> What’s the status of my complaint?

