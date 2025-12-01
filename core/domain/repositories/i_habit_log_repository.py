from abc import ABC, abstractmethod
from typing import Optional

from ..entities.habit_log import HabitLog


class IHabitLogRepository(ABC):
    @abstractmethod
    async def save(self, habit_log: HabitLog) -> None:
        pass

    @abstractmethod
    async def find_all(self, habit_id: str) -> Optional[list[HabitLog]]:
        pass
