import streamlit as st

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Safe Document import: try known package locations and otherwise provide
# a minimal local fallback so the app doesn't crash when langchain schema
# isn't installed under the expected package name.
try:
    from langchain_core.schema import Document as LC_Document
except Exception:
    try:
        from langchain.schema import Document as LC_Document
    except Exception:
        class LC_Document:
            def __init__(self, page_content, metadata=None):
                self.page_content = page_content
                self.metadata = metadata or {}

st.set_page_config(page_title="C++ RAG ChatBot")
st.title("C++ RAG ChatBot")
st.write("Ask any question related to C++ Introduction")

@st.cache_resource
def load_vectorstore():

    file_path = r"D:\genai1\C++_Introduction.txt"

    # Try using TextLoader (with utf-8). If it fails (encoding issues),
    # fall back to reading the file bytes and decoding with multiple encodings.
    try:
        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()
    except Exception:
        encodings = ["utf-8", "cp1252", "latin-1"]
        content = None
        for enc in encodings:
            try:
                with open(file_path, "rb") as f:
                    raw = f.read()
                content = raw.decode(enc)
                break
            except Exception:
                content = None
                continue

        if content is None:
            # As a last resort, decode with replacement to avoid crashes.
            with open(file_path, "rb") as f:
                content = f.read().decode("utf-8", errors="replace")

        documents = [LC_Document(page_content=content, metadata={"source": file_path})]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    finalDocuments = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db=FAISS.from_documents(finalDocuments,embeddings)
    return db

db = load_vectorstore()
query = st.text_input("Enter your question here")
if query:
    docs = db.similarity_search(query, k=3)
    st.subheader("Relevant Information:")
    for i,doc in enumerate(docs):
        st.markdown(f"**Document {i+1}:**")
        st.write(doc.page_content)