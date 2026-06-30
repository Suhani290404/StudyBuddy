from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Split extracted text into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks