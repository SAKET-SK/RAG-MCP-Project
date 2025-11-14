IntelliHR - RAG-Enabled AI Assistant with MCP Architecture

<img src="https://img.shields.io/badge/Python-3.11+-blue.svg"> <img src="https://img.shields.io/badge/Streamlit-1.28+-red.svg"> <img src="https://img.shields.io/badge/Groq-LLM-green.svg"> <img src="https://img.shields.io/badge/License-MIT-yellow.svg">

An intelligent HR assistant that orchestrates multiple data sources using Model Context Protocol (MCP) and Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses.

Built as a capstone project to demonstrate practical AI/ML system design and full-stack development.

---

<h3>Highlights</h3>

<ul>
  <li> Smart Orchestration - LLM intelligently routes queries to appropriate data sources </li>
  <li> RAG Integration - Semantic search over policy documents with zero hallucination </li>
  <li> Beautiful UI - Modern glassmorphism design with dark theme </li>
  <li> Fast Responses - Sub-2 second query processing with Groq's llama-3.3-70b </li>
  <li> Context-Aware - Actually reads and respects document confidentiality markers </li>
  <li> Real-time Analytics - Track queries, tools used, and system performance </li>
</ul>

---

<h3>Architecture</h3>

```
┌─────────────────────────────────────────────┐
│          User Interface (Streamlit)         │
│  Glassmorphism UI • Dark Theme • Analytics  │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│     Orchestrator (Groq LLM)                 │
│  llama-3.3-70b-versatile                    │
│  • Function Calling                         │
│  • Tool Selection                           │
│  • Response Generation                      │
└────────────────┬────────────────────────────┘
                 │
        ┌────────┴─────────┐
        │  MCP Framework   │
        └────────┬─────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
    ▼            ▼            ▼
┌─────────┐ ┌──────────┐ ┌─────────┐
│Database │ │Filesystem│ │   RAG   │
│ Server  │ │  Server  │ │ Server  │
├─────────┤ ├──────────┤ ├─────────┤
│ SQLite  │ │Text Files│ │ChromaDB │
│Employee │ │Announce- │ │Policies │
│Records  │ │ments     │ │(PDFs)   │
└─────────┘ └──────────┘ └─────────┘
```

How it works:

<ul>
  <li> User Query → Enters question in natural language </li>
  <li> Orchestrator → LLM analyzes and selects appropriate tools </li>
  <li> MCP Servers → Execute queries on respective data sources </li>
  <li> Response → LLM combines results into coherent answer </li>
</ul>

---

<h3>Tech Stack</h3>

Core Technologies:
<ul>
<li> Python 3.11+ - Primary language </li>
<li> Streamlit - Web UI framework </li>
<li> Groq API - LLM inference (llama-3.3-70b-versatile) </li>
<li> SQLite - Employee database </li>
<li> ChromaDB - Vector database for RAG </li>
<li> LangChain - RAG pipeline orchestration <li> 
</ul>

Key Libraries:
<ul>
<li> langchain - Document processing and RAG </li>
<li> langchain-groq - Groq LLM integration </li>
<li> langchain-huggingface - Embeddings (all-MiniLM-L6-v2) </li>
<li> chromadb - Vector storage </li>
<li> pypdf - PDF document loading </li>
<li> asyncio - Asynchronous operations </li>
</ul>

Design:
<ul>
<li> Custom CSS with glassmorphism </li>
<li> Responsive design </li>
<li> Dark theme with purple gradient </li>
<li> SVG architecture diagrams </li>
</ul>
---

