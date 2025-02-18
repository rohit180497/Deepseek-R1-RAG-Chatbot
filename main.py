import streamlit as st
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from utils import process_documents, get_retriever
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

# 🎓 New Project Name: ScholarChat AI
st.set_page_config(
    page_title="ScholarChat AI 📖",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Custom prompt template
def get_custom_prompt():
    """Define and return the custom prompt template."""
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are ScholarChat AI, a smart educational assistant designed to help students understand their textbooks. Follow these guidelines:\n"
            "1. Use information only from the uploaded PDFs.\n"
            "2. Explain in a clear and simple way (10th-grade level).\n"
            "3. If no relevant info is found, say: 'I cannot find relevant information in the provided documents.'\n"
            "4. Do not make assumptions or generate extra content.\n"
            "5. Keep answers **concise, structured, and exam-friendly.**\n"
            "6. Use **bullet points, step-by-step explanations, and examples** to clarify concepts.\n"
            "7. Ask the student if they need further clarification.\n"
        ),
        HumanMessagePromptTemplate.from_template(
            "Context:\n{context}\n\n"
            "Question: {question}\n\n"
            "Provide a **clear, well-structured answer** based on the provided context. **Use examples** when necessary and ensure the response is easy to understand."
        )
    ])

# 🧠 Initialize QA Chain
def initialize_qa_chain():
    if not st.session_state.qa_chain and st.session_state.vector_store:
        llm = ChatOllama(model="deepseek-r1:1.5b",
                        temperature=0.3, 
                        base_url="http://127.0.0.1:11434")
        retriever = get_retriever()
        st.session_state.qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": get_custom_prompt()}
        )
    return st.session_state.qa_chain

# 🔄 Initialize chatbot session state
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None

# 🎨 Sidebar: File Upload & Instructions
def display_sidebar():
    with st.sidebar:
        st.markdown("## 📌 ScholarChat AI - Upload Your Study Material")
        st.info("""
        **How to Use ScholarChat AI:**
        1. Upload one or more **PDF textbooks**.
        2. Click **'Create Knowledge Base'**.
        3. Once processed, start **chatting with ScholarChat AI!** 🎓🤖
        """)

        # 🎯 File uploader
        pdfs = st.file_uploader(
            "📂 Upload PDF documents", 
            type="pdf",
            accept_multiple_files=True
        )

        # 🚀 Action Button - Process PDFs
        if st.button("📚 Create Knowledge Base", use_container_width=True):
            if not pdfs:
                st.warning("⚠️ Please upload PDF documents first!")
                return

            try:
                with st.spinner("🔍 Processing documents... This may take a moment."):
                    vector_store = process_documents(pdfs)
                    st.session_state.vector_store = vector_store
                    st.session_state.qa_chain = None  # Reset QA chain when new docs are uploaded
                st.success("✅ Knowledge base created successfully! Start asking questions.")
            except Exception as e:
                st.error(f"❌ Error processing documents: {str(e)}")

# 💬 Chat Interface
def chat_interface():
    st.title("📖 ScholarChat AI - Your Textbook Assistant")
    st.markdown("_Ask anything about your uploaded documents! ScholarChat AI will provide precise, exam-friendly answers._")

    # 🎨 Custom Chat Styling
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # ✍️ User Input
    if prompt := st.chat_input("🔍 Ask about your documents..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            with st.spinner("🤖 Thinking..."):
                try:
                    qa_chain = initialize_qa_chain()
                    if not qa_chain:
                        full_response = "⚠️ Please upload and process your PDF documents first."
                    else:
                        response = qa_chain.invoke({"query": prompt})
                        full_response = response["result"]
                except Exception as e:
                    full_response = f"❌ Error: {str(e)}"

            # 💡 Show AI Response
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# 🏁 Main Function
def main():
    initialize_session_state()
    display_sidebar()
    chat_interface()

if __name__ == "__main__":
    main()
