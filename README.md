# 🎓 ScholarChat AI - Smart Textbook Chatbot

![ScholarChat AI](https://img.shields.io/badge/DeepSeek-AI%20Chatbot-blue?style=for-the-badge)  
A **Streamlit-based AI chatbot** that allows students to interact with their **textbooks** using **DeepSeek 1.5B LLM** and **vector-based retrieval** for precise answers from uploaded PDFs.

---

## 🚀 Features
✅ **PDF-Based Question Answering** – Upload documents and chat with an AI that retrieves relevant content.  
✅ **DeepSeek-1.5B AI Model** – Uses **DeepSeek-1.5B** for efficient and context-aware responses.  
✅ **Retrieval-Augmented Generation (RAG)** – Uses **ChromaDB** for vector-based retrieval.  
✅ **Streamlit Web Interface** – Simple, user-friendly chatbot interface.  
✅ **Supports Multiple PDFs** – Process and query multiple textbooks at once.  

---

## 🏗️ Project Architecture

```
📂 ScholarChat AI
│── 📜 main.py              # Streamlit chatbot UI & interaction
│── 📜 utils.py             # PDF processing & vector store functions
│── 📂 chroma_db            # Persisted vector embeddings (generated dynamically)
│── 📄 README.md            # Project documentation
│── 📦 requirements.txt     # Python dependencies
```

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/ScholarChatAI.git
cd ScholarChatAI
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Download DeepSeek Model**
Ensure you have **Ollama installed** and **DeepSeek-1.5B** model downloaded:
```sh
ollama pull deepseek-r1:1.5b
```

### **5️⃣ Run the Application**
```sh
streamlit run main.py
```

---

## 🖥️ Usage Guide

### **1️⃣ Upload PDFs**
- Click **Upload PDF Documents** in the sidebar.
- Click **Create Knowledge Base** to process the documents.

### **2️⃣ Ask Questions**
- Type your query in the **chat input**.
- The chatbot **retrieves relevant content** and **generates AI responses**.

### **3️⃣ Get Precise Answers**
- The AI **only answers from the uploaded PDFs**.
- If content is missing, it responds:  
  _"I cannot find relevant information in the provided documents."_

---

## ⚙️ How It Works

### **🔹 Vector-Based Retrieval (RAG)**
- Converts **PDF text** into **vector embeddings** using `nomic-embed-text`.
- Stores them in **ChromaDB** for fast lookups.
- Uses **Maximum Marginal Relevance (MMR)** search for precise retrieval.

### **🔹 AI-Powered Chatbot**
- Uses **DeepSeek-1.5B** via `ChatOllama`.
- Generates **exam-friendly responses** with examples.
- Follows **structured, educational guidelines**.

---

## 📜 Example Query

---

## 🏗️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Streamlit** | Web interface for chatbot |
| **LangChain** | AI model interaction |
| **ChromaDB** | Vector-based document retrieval |
| **Ollama** | Local AI model inference |
| **DeepSeek-1.5B** | AI model for generating responses |

---

## 📌 TODO & Future Improvements
- ✅ Add support for **custom LLM models**.
- ✅ Improve **retrieval accuracy** for multi-document queries.
- 🚀 Implement **fine-tuning options** for specific subjects.
- 🚀 Add **support for non-English documents**.

---

## 🤝 Acknowledgments
- **LangChain** – For integrating RAG pipelines.
- **DeepSeek** – For providing high-quality AI models.
- **Streamlit** – For the intuitive web interface.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🌟 Contributing
Pull requests are welcome!  
For major changes, open an issue first to discuss your proposal.

1. **Fork the repo**
2. **Create a feature branch** (`git checkout -b feature-branch`)
3. **Commit changes** (`git commit -m "Added new feature"`)
4. **Push to branch** (`git push origin feature-branch`)
5. **Open a PR** on GitHub

---

## 📬 Contact
For issues or feedback, open an issue or contact:
📧 Email: [kosamkar.r@northeastern.com]  
🌐 GitHub: [github.com/rohit180497]
