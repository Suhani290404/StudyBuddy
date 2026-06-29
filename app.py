import streamlit as st
from src.pdf_loader import load_pdf
st.set_page_config(
    page_title="StudyBuddy AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyBuddy AI")
st.write("Your AI-powered study assistant.")

# Sidebar
with st.sidebar:
    st.header("📂 Upload Notes")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )
if uploaded_file is not None:
    st.success("PDF uploaded successfully! ✅")

    st.write("### File Name")
    st.write(uploaded_file.name)

    pdf_text = load_pdf(uploaded_file)

    st.write("### Extracted Text")

    st.text(pdf_text[:3000])