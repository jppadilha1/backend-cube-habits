from typing import Optional

from ...domain.entities import HabitLog
from ...domain.repositories import IHabitLogRepository


class MockHabitLogRepository(IHabitLogRepository):
    def __init__(self):
        self.logs: list[HabitLog] = []

    async def save(self, habit_log: HabitLog) -> None:
        self.logs.append(habit_log)

    async def find_all(self, habit_id: str) -> Optional[list[HabitLog]]:
        filtered = [log for log in self.logs if log.habit_id == habit_id]
        return filtered if len(filtered) > 0 else None

    def reset(self) -> None:
        self.logs = []
