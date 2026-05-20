import os
from langchain_groq import ChatGroq
from app.planner import get_app

def main():
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        print('Error: GROQ_API_KEY environment variable not set.')
        return

    llm = ChatGroq(temperature=0, model_name='llama-3.3-70b-versatile', api_key=api_key)
    app = get_app(llm)

    config = {'configurable': {'thread_id': '42'}}
    inputs = {
        'city': 'Bangalore',
        'interests': ['Cubbon Park', 'Bangalore Palace'],
        'messages': [],
        'itinerary': '',
        'budget_status': 'Pending',
        'total_estimated_cost': 0.0
    }

    print('--- Starting Multi-Agent Planner ---')
    for output in app.stream(inputs, config=config):
        for node, values in output.items():
            print(f'Node "{node}" finished.')

    final_values = app.get_state(config).values
    print('\n--- FINAL ITINERARY ---')
    print(final_values.get('itinerary'))

if __name__ == "__main__":
    main()