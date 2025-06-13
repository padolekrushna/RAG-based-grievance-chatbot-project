from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def create_vector_store_from_pdf(pdf_path="data/grievance_policy.pdf", persist_path="faiss_index"):
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
    docs = db.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in docs])
