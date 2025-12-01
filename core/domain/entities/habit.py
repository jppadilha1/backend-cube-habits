import dataclasses

from core.domain.value_objects import Description


@dataclasses.dataclass
class Habit:
    id: str
    user_id: str
    description: Description
    created_at: str
    updated_at: str
