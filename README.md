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

<h3>Features</h3>

Current Features (v1.0)

✅ Multi-Source Querying

- Employee database search (name, department, ID)
- Announcement retrieval (holidays, events, updates)
- Policy document search with RAG

✅ Intelligent Routing

- LLM automatically selects correct data source
- Multi-tool queries supported
- Context-aware responses

✅ Professional UI

- Real-time chat interface
- Session statistics tracking
- Tool usage visualization
- Query history with expandable details

✅ Data Sources

- 10 employee records
- 4 announcement files
- 3 policy documents (Leave, POSH, Salary)

System Capabilities

- 9 Tools across 3 MCP servers
- Sub-2s average response time
- Zero hallucination with RAG
- Conversation memory for follow-up questions

---

<h3>Installation</h3>

Prerequisites:
- Python 3.11 or higher
- Groq API key (Get one free)

Step 1 : Clone the repository

```
git clone https://github.com/yourusername/intellihr-rag-mcp.git
cd intellihr-rag-mcp
```

Step 2 : Create virtual environment

```
python -m venv .venv

# Activate
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

Step 3 : Install Dependencies

```
pip install -r requirements.txt
```

Step 4 : Set up environment variables

```
# Windows PowerShell
$env:GROQ_API_KEY="your-groq-api-key-here"

# Linux/Mac
export GROQ_API_KEY="your-groq-api-key-here"
```

Step 5 : Initialize the Database

```
python setup_database.py
```

Step 6 : Run the mcp servers to initialize them

```
python mcp_servers/database_server.py
python mcp_servers/rag_server.py
python mcp_servers/file_system_server.py
```

Step 7 : Run the orchestrator

```
python orchestrator.py
```

Step 6 : Run the Application

```
streamlit run app.py
```

The app will open in your browser at http://localhost:8501

---

<h3>Project Structure</h3>

```
intellihr-rag-mcp/
├── app.py                      # Main Streamlit application
├── orchestrator.py             # LLM orchestrator for tool routing
├── setup_database.py           # Database initialization script
├── requirements.txt            # Python dependencies
│
├── mcp_servers/               # MCP Server implementations
│   ├── database_server.py     # Employee database server
│   ├── filesystem_server.py   # Announcements server
│   └── rag_server.py          # Policy documents RAG server
│
├── ui/                        # UI components
│   ├── __init__.py
│   └── styles.py              # Custom CSS styles
│
├── data/                      # Data storage
│   ├── announcements/         # Text files for announcements
│   ├── policies/              # PDF policy documents
│   └── chroma_store/          # ChromaDB vector database
│
├── employees.db               # SQLite database (created after setup)
└── README.md                  # This file
```
