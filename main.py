from google.colab import userdata
import os
from langchain_groq import ChatGroq
from app.planner import get_app

def main():

    # Load API key securely
    groq_api_key = userdata.get("GROQ_API_KEY")

    if not groq_api_key:
        print("GROQ_API_KEY not found")
        return

    # Initialize model
    llm = ChatGroq(
        temperature=0,
        model_name="llama-3.3-70b-versatile",
        api_key=groq_api_key
    )

    # Build app
    app = get_app(llm)

    config = {
        "configurable": {
            "thread_id": "1"
        }
    }

    inputs = {
        "city": "Paris",
        "interests": ["Eiffel Tower", "Louvre"],
        "messages": [],
        "itinerary": "",
        "budget_status": "Pending",
        "total_estimated_cost": 0.0
    }

    print("---- Running Multi-Agent Planner ----")

    for output in app.stream(inputs, config=config):
        for node, value in output.items():
            print(f"Node '{node}' completed")

    final_state = app.get_state(config).values

    print("\n--- FINAL ITINERARY ---")
    print(final_state.get("itinerary"))

if __name__ == "__main__":
    main()
