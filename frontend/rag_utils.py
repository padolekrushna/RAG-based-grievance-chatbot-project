!pip install langchain openai faiss-cpu tiktoken unstructured python-dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

def create_vector_store_from_pdf(pdf_path, persist_path="faiss_index"):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(pages)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(persist_path)

def load_vector_store(persist_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(persist_path, embeddings)

def get_rag_context(query):
    db = load_vector_store()
    matches = db.similarity_search(query, k=2)
    return "\n\n".join([match.page_content for match in matches])
