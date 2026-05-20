
import os
from typing import List, TypedDict, Annotated
from langgraph.graph import StateGraph, END
from .models.itinerary import Itinerary

class PlannerState(TypedDict):
    messages: list
    city: str
    interests: List[str]
    itinerary: str

# Note: This file would normally contain the full create_itinerary logic
# and graph compilation for use in a modular deployment.
