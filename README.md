# 🤖 AI-Powered DevOps & Research Assistant

## 🚀 Overview

This project is an AI-powered system that combines **Retrieval-Augmented Generation (RAG)** with **DevOps monitoring, security detection, and research assistance**.

It analyzes logs, detects issues, suggests fixes, and allows users to query both logs and research documents intelligently.

---

## 🧠 Features

### 🔍 RAG-Based Log Analysis

* Retrieves relevant logs using FAISS vector database
* Provides intelligent debugging insights

### 📄 Research Assistant (PDF Support)

* Upload research papers
* Ask questions or get summaries

### 🤖 AI-Powered Insights

* Uses Gemini AI for explanation and reasoning
* Structured responses (Issue, Cause, Fix)

### ⚡ Self-Healing Simulation

* Suggests actionable fixes
* "Apply Fix" button for demonstration

### 🔐 Security Detection

* Detects suspicious patterns (DDoS, unauthorized access)

### 📊 Risk Scoring

* Generates a dynamic risk score for system health

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI Model:** Gemini (Google Generative AI)
* **RAG:** LangChain + FAISS
* **Embeddings:** HuggingFace (MiniLM)

---

## 📂 Project Structure

```
├── app.py
├── rag/
│   └── ingest.py
├── vectorstore/
├── logs/
├── test_query.py
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧪 Example Queries

* Why did build fail?
* How to fix memory issue?
* Explain this research paper
* Detect security threats

---

## 🧠 How It Works

1. Logs and documents are converted into embeddings
2. Stored in FAISS vector database
3. Relevant context is retrieved using similarity search
4. Gemini AI generates accurate responses

---

## 🎯 Use Cases

* DevOps Monitoring
* Debugging CI/CD Pipelines
* Research Paper Analysis
* Security Threat Detection

---

## 🏆 Future Enhancements

* Real-time CI/CD integration
* Docker/Kubernetes monitoring
* Advanced anomaly detection
* Multi-user dashboard

---

## 👨‍💻 Author

**Abhishekagouda Patil**
B.Tech Computer Science

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
