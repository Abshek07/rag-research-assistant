from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load PDF
loader = PyPDFLoader("data/paper1.pdf")
documents = loader.load()

print("Pages loaded:", len(documents))

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Total chunks:", len(chunks))

# Create embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store vectors in FAISS database
vectorstore = FAISS.from_documents(chunks, embeddings)

print("Vector database created successfully!")

# Test a query
query = "What is MedExChain?"

docs = vectorstore.similarity_search(query, k=3)

print("\nTop relevant chunks:\n")

for doc in docs:
    print(doc.page_content[:500])
    print("\n------------------\n")