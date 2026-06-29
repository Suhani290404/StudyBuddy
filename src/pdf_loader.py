from pypdf import PdfReader


def load_pdf(uploaded_file):
    """
    Read all text from an uploaded PDF.
    """

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text