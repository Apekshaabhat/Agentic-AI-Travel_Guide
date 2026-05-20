# ✈️ Agentic AI Travel Guide

A stateful multi-agent AI travel planning system built using LangGraph, Groq (Llama 3.3), and Gradio.

This project demonstrates agentic AI workflows using graph-based orchestration, structured outputs, memory checkpointing, and modular backend architecture.

---

# 🚀 Features

- Multi-Agent Workflow using LangGraph
- Structured itinerary generation using Pydantic
- Budget validation agent
- Stateful graph execution with MemorySaver
- Secure API key handling using environment variables
- Modular Python project structure
- Interactive Gradio interface
- Input validation and error handling

---

# 🧠 Workflow Architecture

The system uses a multi-agent graph workflow:

Entry
↓
Planner Agent
↓
Budget Validator Agent
↓
End

## Planner Agent

Generates:
- Morning itinerary
- Afternoon itinerary
- Evening itinerary
- Food recommendations

## Validator Agent

Analyzes:
- Estimated travel cost
- Budget feasibility
- General financial validation

---

# 🛠️ Tech Stack

- LangGraph
- LangChain
- Groq API (Llama 3.3)
- Gradio
- Pydantic
- Python

---

# 📂 Project Structure

```text
Agentic-AI-Travel_Guide/
│
├── app/
│   ├── __init__.py
│   └── planner.py
│
├── models/
│   ├── __init__.py
│   └── itinerary.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
