import streamlit as st
import google.generativeai as genai

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# 🔑 Replace with your NEW API key (never share publicly)
genai.configure(api_key="AIzaSyCJrltRRDvVv9uNuhQOVGZRZGsHtEwEL7s")

# 🎯 Page Title
st.title("🤖 AI DevOps Assistant")

# 💬 Input
query = st.text_input("Ask your question:")

# ⚡ Fix suggestion logic
def suggest_fix(context):
    context = context.lower()

    if "port" in context:
        return "Run: netstat -ano | findstr :3000 → then kill the process using taskkill"
    
    elif "environment variable" in context:
        return "Add required environment variable (e.g., DB_HOST) in your .env file and restart"
    
    elif "memory" in context:
        return "Increase Docker/container memory or optimize application usage"
    
    else:
        return "Check logs manually for more details"

# 🚀 Main logic
if query:
    # Load embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Load vector DB
    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Retrieve relevant logs
    docs = db.similarity_search(query)
    context = "\n".join([doc.page_content for doc in docs])

    # 🤖 Gemini model (working for your account)
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    # 🧠 Prompt
    prompt = f"""
    You are a DevOps assistant.

    Logs:
    {context}

    Question:
    {query}

    Explain the issue clearly and give a fix.
    """

    # 🔄 Generate response
    response = model.generate_content(prompt)

    # 📢 Show answer
    st.write("### 🧠 Answer:")
    try:
        st.write(response.text)
    except:
        st.write("⚠️ No response received. Try again.")

    # ⚡ Suggested fix
    fix = suggest_fix(context)

    st.write("### ⚡ Suggested Fix:")
    st.write(fix)

    # 🔧 Self-healing button (demo)
    if st.button("🔧 Apply Fix"):
        st.success("Simulated fix applied successfully!")