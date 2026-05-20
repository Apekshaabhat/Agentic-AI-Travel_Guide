# LangGraph Secure Travel Planner

A secure, structured travel itinerary generator built with LangGraph, LangChain, and Groq (Llama 3).

## Features
- **Structured Output**: Uses Pydantic to ensure itineraries always include Morning, Afternoon, Evening, and Food suggestions.
- **Input Validation**: Regex and Pydantic-based validation for city names and interests.
- **Secure**: No hardcoded API keys; uses `.env` for credential management.
- **UI**: Interactive Gradio interface for easy generation.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file and add: `GROQ_API_KEY=your_key_here`.
4. Run the notebook or main script.
