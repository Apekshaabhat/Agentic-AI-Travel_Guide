
from typing import List
from pydantic import BaseModel, Field

class Itinerary(BaseModel):
    morning: str = Field(description='Activities for the morning')
    afternoon: str = Field(description='Activities for the afternoon')
    evening: str = Field(description='Activities for the evening')
    food_suggestions: List[str] = Field(description='Recommended local eateries')
