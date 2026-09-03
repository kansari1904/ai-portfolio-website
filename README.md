````markdown
# Khalid Ansari — AI Engineer Portfolio

> AI-powered personal portfolio with an integrated AI Recruiter Assistant.

🌐 **Portfolio:** Coming soon  
💼 **LinkedIn:** https://www.linkedin.com/in/kansari1904/  
💻 **GitHub:** https://github.com/kansari1904  
📧 **Email:** kansari1904@gmail.com

---

## Overview

This project is a modern, responsive developer portfolio built to showcase my experience in software development and AI engineering.

The portfolio includes an AI Recruiter Assistant that allows recruiters and visitors to ask questions about my background, technical skills, education, and projects.

Instead of relying entirely on an LLM for every question, the backend uses a routing architecture that selects the most appropriate response strategy.

```text
                         User Question
                              │
                              ▼
                       Query Router
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
             FAQ        Portfolio Fact       RAG
              │               │               │
              ▼               ▼               ▼
         faq.json       portfolio.json      Chroma
              │               │               │
              └───────────────┴───────────────┘
                              │
                              ▼
                         Final Answer
````

---

## Key Features

### Portfolio

* Responsive modern UI
* Mobile, tablet, and desktop support
* Dark-themed interface
* Project showcase
* About section
* Contact section
* GitHub and LinkedIn integration

### AI Recruiter Assistant

* Recruiter-focused question answering
* FAQ-based direct responses
* Portfolio knowledge retrieval
* Retrieval-Augmented Generation (RAG)
* LLM-powered responses
* Streaming responses
* Markdown rendering
* Suggested recruiter questions
* Copy response functionality
* Retry handling
* Conversation reset

### Backend

* FastAPI REST API
* Modular service architecture
* Pydantic validation
* CORS configuration
* LLM service abstraction
* Retrieval service
* Question routing
* Knowledge-base management

---

# Architecture

```text
┌──────────────────────────────────────────────┐
│                  React UI                    │
│                                              │
│  Hero → About → Projects → AI Assistant     │
│                              ↓               │
│                         Chat Interface       │
└───────────────────────┬──────────────────────┘
                        │
                        │ HTTP / Streaming
                        ▼
┌──────────────────────────────────────────────┐
│                FastAPI Backend               │
│                                              │
│                 Query Router                 │
│                      │                       │
│          ┌───────────┼───────────┐           │
│          ▼           ▼           ▼           │
│         FAQ       Portfolio      RAG         │
│          │           │           │           │
│       faq.json   portfolio.json  Chroma      │
│                                  │           │
│                                  ▼           │
│                                  LLM         │
└──────────────────────────────────────────────┘
```

---

# Tech Stack

## Frontend

* React
* Vite
* Tailwind CSS
* React Markdown
* JavaScript

## Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

## AI Engineering

* LLM APIs
* LangChain
* Retrieval-Augmented Generation
* Chroma
* HuggingFace Embeddings
* Sentence Transformers
* Prompt Engineering
* Streaming responses

---

# Project Structure

```text
khalid-portfolio/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── About.jsx
│   │   │   ├── Projects.jsx
│   │   │   ├── Contact.jsx
│   │   │   └── Footer.jsx
│   │   │
│   │   ├── services/
│   │   │   └── chatApi.js
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── rag/
│   │   └── utils/
│   │
│   ├── data/
│   │   └── knowledge/
│   │       ├── faq.json
│   │       └── portfolio.json
│   │
│   ├── scripts/
│   ├── tests/
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

# Featured Projects

## DocuMind-AI

An AI-powered document assistant that allows users to upload PDF documents and interact with their content.

### Features

* PDF processing
* AI-generated summaries
* Flashcard generation
* Quiz generation
* Document-based chat

### Technologies

`React` `Tailwind CSS` `Node.js` `Express` `MongoDB` `Gemini API`

---

## AI Customer Support Agent

An AI-powered customer support system focused on knowledge retrieval and context-aware responses.

### Features

* RAG-based knowledge retrieval
* LLM-powered responses
* Context-aware support
* AI workflow orchestration

### Technologies

`Python` `FastAPI` `LangChain` `RAG` `LLM APIs` `Vector Database`

---

## CodeGyan

A full-stack e-learning platform built using the MERN stack.

### Features

* Responsive React frontend
* REST API backend
* MongoDB database
* State management
* Educational content platform

### Technologies

`React` `Node.js` `Express` `MongoDB` `Redux Toolkit` `Tailwind CSS`

---

# API Endpoints

The backend exposes the following primary endpoints:

```text
POST /api/chat
POST /api/chat/stream

GET /api/chat/suggestions
GET /api/chat/faq/{faq_id}
```

FastAPI also provides interactive API documentation:

```text
/docs
```

---

# Local Development

## 1. Clone the repository

```bash
git clone https://github.com/kansari1904/khalid-portfolio.git

cd khalid-portfolio
```

---

# Frontend Setup

```bash
cd frontend

npm install
```

Create:

```text
frontend/.env
```

Add:

```env
VITE_API_BASE_URL=http://localhost:8000/api
```

Run:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# Backend Setup

Open another terminal:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create:

```text
backend/.env
```

Add:

```env
OPENROUTER_API_KEY=your_api_key
FRONTEND_URL=http://localhost:5173
```

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

---

# Environment Variables

## Frontend

```env
VITE_API_BASE_URL=
```

## Backend

```env
OPENROUTER_API_KEY=
FRONTEND_URL=
```

Never commit actual API keys or `.env` files.

---

# Deployment

The recommended production architecture is:

```text
             ┌──────────────┐
             │   Vercel     │
             │   React UI   │
             └──────┬───────┘
                    │
                    │ HTTPS
                    ▼
             ┌──────────────┐
             │   Render     │
             │   FastAPI    │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ LLM / Chroma │
             │  Knowledge   │
             └──────────────┘
```

---

# Future Improvements

* Custom domain
* Project demo links
* GitHub project links
* Analytics
* Conversation feedback
* Authentication for private recruiter data
* Improved evaluation and observability
* Automated testing and CI/CD

---

# Author

## Khalid Ansari

Computer Science & Engineering graduate focused on Software Development and AI Engineering.

### Areas of Interest

* AI Engineering
* LLM Applications
* RAG
* Agentic AI
* Full-Stack Development
* Backend Engineering

### Connect

* GitHub: https://github.com/kansari1904
* LinkedIn: https://www.linkedin.com/in/kansari1904/
* Email: [kansari1904@gmail.com](mailto:kansari1904@gmail.com)

```
```
