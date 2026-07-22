# CodeAtlas AI

> **An AI-powered repository intelligence platform that enables developers to understand, explore, and query large codebases using Retrieval-Augmented Generation (RAG), semantic search, and Large Language Models (LLMs).**

<p align="center">
  <img src="assets/screenshots/landing.png" alt="Landing Page" width="900"/>
</p>

---

## Overview

Understanding unfamiliar codebases can be time-consuming. CodeAtlas AI simplifies this process by indexing a repository, extracting its structure, generating semantic embeddings, and allowing developers to ask natural language questions about the project.

Instead of manually navigating files, developers can interact with the repository through an AI assistant that retrieves the most relevant code before generating contextual answers.

---

## Features

* Repository indexing
* AI-powered repository Q&A
* Retrieval-Augmented Generation (RAG)
* Semantic code retrieval using embeddings
* FAISS vector similarity search
* Tree-sitter based source code parsing
* Monaco Editor based code viewer
* Source attribution for every AI response
* Support for both local (Ollama) and hosted (Grok API) LLMs
* Interactive repository explorer

---

## Architecture

<p align="center">
  <img src="assets/architecture.png" alt="Architecture" width="900"/>
</p>

### High-Level Workflow

```text
                 User
                   │
                   ▼
           React + Vite Frontend
                   │
            FastAPI REST API
                   │
      ┌────────────┴────────────┐
      │                         │
Repository Scanner        AI Services
      │                         │
 Tree-sitter Parser      Grok API / Ollama
      │                         │
 Embeddings + FAISS      Prompt Builder
      └────────────┬────────────┘
                   │
             AI Generated Answer
```

---

## Screenshots

### Landing Page

![Landing](assets/screenshots/landing.png)

---

### Workspace

![Workspace](assets/screenshots/workspace.png)

---

### AI Chat

![Chat](assets/screenshots/chat.png)

---

### File Viewer

![File Viewer](assets/screenshots/fileviewer.png)

---

## Tech Stack

### Frontend

* React
* TypeScript
* Vite
* Tailwind CSS
* Monaco Editor

### Backend

* Python
* FastAPI
* REST APIs
* Tree-sitter
* FAISS

### AI Technologies

* Retrieval-Augmented Generation (RAG)
* Semantic Embeddings
* Prompt Engineering
* Ollama
* Grok API
* Large Language Models (LLMs)

---

## Project Structure

```text
.
├── backend
│   ├── app
│   ├── api
│   ├── services
│   ├── retrieval
│   ├── llm
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── components
│   ├── pages
│   ├── services
│   └── package.json
│
├── assets
│   ├── architecture.png
│   └── screenshots
│
└── README.md
```

---

## Getting Started

### Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <repository-name>
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## Environment Variables

Create a `.env` file inside the backend directory.

```env
APP_NAME=CodeAtlas AI
API_VERSION=v1

LLM_PROVIDER=groq

OLLAMA_MODEL=qwen2.5-coder:7b
OLLAMA_HOST=http://localhost:11434

GROQ_API_KEY=YOUR_API_KEY

FRONTEND_ORIGIN=http://localhost:5173
```

---

## How It Works

1. User selects a local repository.
2. The repository is scanned and parsed using Tree-sitter.
3. Source code is chunked and converted into semantic embeddings.
4. Embeddings are indexed using FAISS.
5. User asks a question.
6. The system retrieves the most relevant code.
7. Context is sent to the configured LLM.
8. The AI generates an answer with relevant source references.

---

## Current Capabilities

* Repository indexing
* Context-aware AI responses
* Source code retrieval
* Repository navigation
* Read-only code viewer
* Semantic search
* Explain selected files
* Local and hosted LLM support

---

## Future Improvements

* GitHub repository support
* Multi-repository indexing
* Conversation history
* Streaming AI responses
* Better ranking and reranking
* Docker support
* Authentication
* Repository summaries
* Repository-wide search filters

---

## Demo

**Live Demo:** *Coming Soon*

**GitHub Repository:** *Add your repository link here*

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* FastAPI
* React
* Monaco Editor
* Tree-sitter
* FAISS
* Ollama
* Grok API


## Deployment Note

The live deployment demonstrates the backend API and application architecture. Repository indexing requires filesystem access to the target repository. Therefore, the complete indexing and RAG workflow is intended to run locally, where the backend can access local repositories. The deployed backend is primarily provided for API demonstration purposes.