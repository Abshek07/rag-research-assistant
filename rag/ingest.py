from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

def ingest_logs():
    # ✅ Hardcoded logs (no file issues anymore)
    text = """
    ERROR: Port 3000 already in use
    Build failed due to missing environment variable DB_HOST
    Container crashed due to out of memory
    """

    documents = [Document(page_content=text)]

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(docs, embeddings)
    db.save_local("vectorstore")

if __name__ == "__main__":
    ingest_logs()