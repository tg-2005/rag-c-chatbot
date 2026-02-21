

# 📘 C++ RAG ChatBot

A Streamlit-based Retrieval-Augmented Generation (RAG) chatbot that answers questions about **C++ concepts** using a custom knowledge base.

This project uses:

* A C++ introduction document as the knowledge source 
* A Streamlit application for the UI 
* FAISS vector database for similarity search
* HuggingFace embeddings for semantic understanding
* Dependencies listed in requirements.txt 

---

## 🚀 Features

* 📂 Loads C++ learning material from a text file
* ✂️ Splits content into semantic chunks
* 🧠 Converts text into vector embeddings
* 🔍 Performs similarity search using FAISS
* 💬 Interactive Streamlit chatbot interface
* ⚡ Fast local retrieval-based answers

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* HuggingFace Embeddings (`all-MiniLM-L6-v2`)
* FAISS (CPU)
* Sentence Transformers

---

## 📁 Project Structure

```
├── chatBot.py              # Streamlit RAG application
├── C++_Introduction.txt    # C++ knowledge base
├── requirements.txt        # Project dependencies
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run chatBot.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 📌 How It Works

1. Loads `C++_Introduction.txt`
2. Splits text into smaller chunks
3. Generates embeddings using HuggingFace model
4. Stores embeddings in FAISS vector store
5. Accepts user question
6. Performs similarity search
7. Displays the most relevant document chunks

---

## 🧠 Example Questions

* What is polymorphism in C++?
* Explain virtual functions.
* What is a copy constructor?
* Difference between class and struct?
* What is inheritance?

---

## ⚠️ Important Notes

* Update the file path inside `chatBot.py` to match your local system:

  ```python
  file_path = r"your_local_path/C++_Introduction.txt"
  ```
* Make sure FAISS is installed correctly for your system.
* This chatbot performs **retrieval only**, not generative answering.

---

## 🔧 Future Improvements

* Add LLM integration for better natural language answers
* Deploy to Streamlit Cloud
* Add file upload feature
* Improve UI styling
* Add multi-document support

---

## 📜 License

This project is open-source and free to use.

---

If you'd like, I can also:

* 🔥 Make it more professional (resume-ready)
* 🎯 Add badges (Python version, license, etc.)
* ☁️ Add Streamlit Cloud deployment instructions
* 🧠 Convert it into a portfolio-style README
* 🏢 Format it for internship/project submission

Just tell me what vibe you’re going for 😄
