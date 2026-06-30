import streamlit as st

from src.pdf_loader import load_pdf
from src.text_splitter import split_text
from src.vector_store import create_vector_store
from src.chatbot import get_conversational_chain


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="StudyBuddy",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyBuddy")
st.write("Your AI-powered study companion.")


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("📂 Upload Notes")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )


# -----------------------------
# Main App
# -----------------------------
if uploaded_file is not None:

    st.success("PDF uploaded successfully! ✅")

    st.write("### File Name")
    st.write(uploaded_file.name)

    # Load PDF
    with st.spinner("Loading PDF..."):
        pdf_text = load_pdf(uploaded_file)

    st.success("PDF loaded")

    # Split text
    with st.spinner("Splitting text..."):
        chunks = split_text(pdf_text)

    st.success(f"Created {len(chunks)} chunks")

    # Create vector database
    with st.spinner("Creating vector store..."):
        vector_store = create_vector_store(chunks)

    st.success("Vector store created")

    # Show extracted text
    st.write("## Extracted Text")
    st.text(pdf_text[:3000])

    st.write("## Number of Chunks")
    st.success(len(chunks))

    st.write("## First Chunk")
    st.text(chunks[0])

    st.divider()

    # -----------------------------
    # Ask Questions
    # -----------------------------
    st.header("💬 Ask Questions About Your PDF")

    user_question = st.text_input(
        "Ask anything from the uploaded PDF:"
    )

    if user_question:

        docs = vector_store.similarity_search(
            user_question,
            k=4
        )

        chain = get_conversational_chain()

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are a helpful study assistant.

Answer ONLY using the information below.

Context:
{context}

Question:
{user_question}

Answer:
"""

        response = chain.invoke(prompt)

        st.subheader("Answer")

        st.write(response.content)