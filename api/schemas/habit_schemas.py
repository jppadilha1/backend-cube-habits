from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator


class HabitCreate(BaseModel):
    description: str = Field(..., min_length=1, max_length=500)


class HabitUpdate(BaseModel):
    description: str = Field(..., min_length=1, max_length=500)


class HabitResponse(BaseModel):
    id: str
    user_id: str
    description: str
    created_at: datetime
    updated_at: datetime

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

        # If 'v' is your Habit entity object, manually map the fields
        return {
            "id": v.id,
            "user_id": v.user_id,
            # Extract string from Description value object
            "description": v.description.value
            if hasattr(v.description, "value")
            else v.description,
            "created_at": v.created_at,
            "updated_at": v.updated_at,
        }
