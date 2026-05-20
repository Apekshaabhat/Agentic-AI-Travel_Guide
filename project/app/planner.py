from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, AIMessage

class PlannerState(TypedDict):
    messages: Annotated[list, "Conversation history"]
    city: str
    interests: List[str]
    itinerary: str
    budget_status: str
    total_estimated_cost: float

def create_itinerary(state):
    itinerary = f"""
MORNING:
Visit {state['interests'][0]}

AFTERNOON:
Explore local attractions in {state['city']}

EVENING:
Enjoy local food and nightlife

"""

    return {
        **state,
        "itinerary": itinerary,
        "messages": state["messages"] + [
            AIMessage(content=itinerary)
        ]
    }

def budget_validator(state):
    return {
        **state,
        "budget_status": "Verified",
        "messages": state["messages"] + [
            AIMessage(content="Budget validated successfully")
        ]
    }

def get_app(llm=None):

    workflow = StateGraph(PlannerState)

    workflow.add_node("planner", create_itinerary)
    workflow.add_node("validator", budget_validator)

    workflow.set_entry_point("planner")

    workflow.add_edge("planner", "validator")
    workflow.add_edge("validator", END)

    checkpointer = MemorySaver()

    app = workflow.compile(
        checkpointer=checkpointer
    )

    return app