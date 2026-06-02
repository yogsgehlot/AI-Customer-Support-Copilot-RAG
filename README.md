# 🤖 AI-Powered Customer Support Copilot (RAG)

An enterprise-grade Retrieval-Augmented Generation (RAG) application that enables users to upload complex documents and extract contextually accurate, natural language answers. The system seamlessly handles document chunking, semantic vector search, and secure LLM-grounded text generation.

This project showcases production-ready Generative AI engineering, combining local embedding extraction with low-latency vector indexing and robust API development.

---

## 📌 Business Problem

Customer support centers and internal operations are often bottlenecked by manual document verification.

Sifting through hundreds of pages of legal agreements, terms of service, and technical manuals is time-consuming and error-prone. This project automates document-grounded question-answering, ensuring support teams or end-users get immediate, highly contextual answers backed by exact source citations.

---

## 🎯 Project Objectives

* Ingest and preprocess multi-format PDF documents dynamically.
* Implement optimized text chunking strategies to preserve contextual integrity.
* Generate dense vector representations using state-of-the-art embedding models.
* Establish a high-performance local vector database using FAISS for low-latency retrieval.
* Synthesize well-grounded, accurate responses using Google's Gemini LLM.
* Expose modular, well-documented endpoints via a FastAPI backend.
* Deliver an intuitive, stateful chat interface built with Streamlit.
* Containerize the entire ecosystem using Docker and Docker Compose for production deployment.

---

## 🏗️ Project Architecture

```text
       PDF Documents
             │
             ▼
    Document Extraction (PyPDF)
             │
             ▼
 Intelligent Text Chunking (LangChain)
             │
             ▼
Vector Embeddings (Sentence Transformers)
             │
             ▼
     FAISS Vector Index
             │
             ▼
   Semantic Retriever ◄─────── User Query
             │                     │
             ▼                     │
Contextual Prompt Generation       │
             │                     │
             ▼                     │
     Gemini 2.5 Flash              │
             │                     │
             ▼                     ▼
     Answer Synthesis ──────► FastAPI Backend
                                   │
                                   ▼
                          Streamlit Chat UI

```

---

## 📂 Project Structure

```text
AI-Customer-Support-Copilot/
│
├── app/
│   └── streamlit_app.py         # Streamlit Chat Interface Frontend
│
├── data/
│   ├── raw/                     # Source PDF Documents
│   └── processed/               # Extracted Text/JSON Data
│
├── logs/                        # Application Activity Logs
│
├── src/
│   ├── api/                     # FastAPI Routing & Endpoints
│   ├── embeddings/              # Embedding Generation Logic
│   ├── ingestion/               # Document Loading Pipelines
│   ├── llm/                     # Gemini Integration & Prompting
│   ├── preprocessing/           # Data Cleaning & Tokenization Scripts
│   └── retriever/               # FAISS Search Engine Logic
│
├── vector_db/                   # Saved FAISS Index Files
│
├── tests/                       # Unit & Integration Tests
│
├── Dockerfile                   # Monolithic App Container Definition
├── docker-compose.yml           # Multi-Container Deployment Specification
├── requirements.txt             # Python Package Dependencies
├── README.md                    # Project Documentation
└── .env                         # Local Environment Secret Store

```

---

## ⚙️ Technologies Used

### Frontend Interface

* Streamlit

### Backend Framework

* FastAPI
* Uvicorn

### Generative AI & NLP

* Gemini 2.5 Flash
* Sentence Transformers (`all-MiniLM-L6-v2`)
* LangChain Text Splitters

### Vector Search Engine

* FAISS (Facebook AI Similarity Search)

### Data Processing

* PyPDF
* Pathlib

### Containerization & Deployment

* Docker
* Docker Compose

---

## 🚀 Installation

Clone Repository

```bash
git clone https://github.com/yogsgehlot/AI-Customer-Support-Copilot.git
cd AI-Customer-Support-Copilot

```

Create Virtual Environment

```bash
python -m venv venv

```

Activate Environment

### Windows

```bash
venv\Scripts\activate

```

### Linux / Mac

```bash
source venv/bin/activate

```

Install Dependencies

```bash
pip install -r requirements.txt

```

---

## 🔑 Environment Configuration

Create a `.env` file in the root directory of the project:

```env
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE

```

> [!TIP]
> You can generate a free or pay-as-you-go API key directly from the [Google AI Studio Console](https://aistudio.google.com/).

---

## 📦 Pipeline Execution

### 1. Prepare Document Corpus

Place your reference PDF files (e.g., `github_terms.pdf`, `stripe_agreement.pdf`, `netflix_terms.pdf`) into the raw data folder: `data/raw/`

### 2. Run Preprocessing Pipeline

Clean raw text data and generate localized structure files:

```bash
python src/preprocessing/create_corpus.py

```

### 3. Generate Smart Text Chunks

Split documents into overlapping text fragments optimized for LLM context windows:

```bash
python src/preprocessing/export_chunks.py

```

### 4. Build and Serialize FAISS Index

Pass chunks through the embedding model and store them inside the vector database:

```bash
python -m src.retriever.build_index

```

---

## 🌐 Running the Infrastructure

### Spin Up FastAPI Backend

```bash
uvicorn src.api.main:app --reload

```

* Interactive Swagger API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Spin Up Streamlit Frontend

In a secondary terminal tab, run:

```bash
streamlit run app/streamlit_app.py

```

* Local Application Web URL: [http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)

---

## 📮 API Specification

### `POST /ask`

#### Request Body

```json
{
  "question": "What is the refund policy for active accounts?"
}

```

#### Response Body

```json
{
  "answer": "Refunds are processed within 30 days of cancellation according to the agreement rules. However, certain subscription tiers may incur a partial processing fee as detailed in Section 4.",
  "sources": [
    "stripe_agreement.pdf",
    "netflix_terms.pdf"
  ]
}

```

---

## 🐳 Docker Deployment

### Standard Docker Build

Build Docker Image:

```bash
docker build -t ai-support-copilot .

```

Run Container:

```bash
docker run -p 8000:8000 --env-file .env ai-support-copilot

```

---

### Docker Compose Multi-Container Setup

To launch both backend service endpoints and user interfaces simultaneously with unified volume networks, simply run:

```bash
docker-compose up --build

```

---

## 📈 Resume Highlights

* **Production-Grade RAG Engineering:** Developed an enterprise-grade Retrieval-Augmented Generation (RAG) system utilizing Gemini, FAISS, FastAPI, and Streamlit.
* **Semantic Search Implementation:** Implemented highly accurate semantic search over corporate document repositories using state-of-the-art Sentence Transformers and dense vector embedding spaces.
* **Scalable Data Pipelines:** Engineered robust data ingestion, regex cleaning, chunking, and deterministic indexing workflows built to ingest complex multi-page PDF documents smoothly.
* **Grounded LLM Generation:** Integrated Gemini LLM architectures to mitigate hallucinations, forcing responses to stay grounded contextually with strict traceable source citations.
* **Containerized Infrastructure:** Configured application code into highly portable environments using Docker and Docker Compose, enabling repeatable orchestration across environments.

---

## 🔮 Future Enhancements

* **Persistent Conversational Memory:** Integrating a PostgreSQL-backed Redis schema to track conversations long-term.
* **Hybrid Vector Search Engine:** Scaling out local FAISS lookups to production-level cloud instances using ChromaDB or Pinecone.
* **Multi-Agent Orchestration:** Upgrading linear RAG calls into an advanced autonomous workflow utilizing LangGraph routing mechanisms.
* **Enterprise Security Standards:** Layering Role-Based Access Controls (RBAC) and OAuth2/JWT token flows over public API endpoints.
* **Cloud Native Infrastructure:** Structuring continuous deployment configurations targeting AWS ECS or managed Kubernetes clusters.

---

## 💼 Author

**Yogesh Gehlot** 

*AI/ML Engineer | Backend Developer*

### Connect With Me

* **GitHub:** [github.com/yogsgehlot](https://github.com/yogsgehlot)
* **LinkedIn:** [linkedin.com/in/yogsgehlot](https://linkedin.com/in/yogsgehlot)
* **X (Twitter):** [x.com/yogsgehlot](https://x.com/yogsgehlot)

---

## 📄 License

This repository is distributed under the terms of the MIT License. Feel free to use it for educational, commercial, or portfolio development purposes.

---

*If you found this system blueprint useful, please consider leaving a ⭐ on the source repository!*