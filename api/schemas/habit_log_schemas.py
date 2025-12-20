from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, model_validator


class HabitLogCreate(BaseModel):
    done_at: Optional[datetime] = None  # Se None, usa datetime.now() no use case


class HabitLogResponse(BaseModel):
    id: int
    habit_id: str
    done_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="before")
    @classmethod
    def map_domain_to_schema(cls, v):
        """
        Intercepts the Domain Entity before validation and extracts
        the specific values needed for the response.
        """
        # If 'v' is a dictionary, return it as is (handling recursion/testing)
        if isinstance(v, dict):
            return v

        # If 'v' is your HabitLog entity object, manually map the fields
        return {
            "id": v.id,
            "habit_id": v.habit_id,
            "done_at": v.done_at,
        }
