import dataclasses


@dataclasses.dataclass
class HabitLog:
    id: str
    habit_id: str
    done_at: str
