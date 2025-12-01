from abc import ABC, abstractmethod
from typing import Optional

from ..entities.habit import Habit


class IHabitRepository(ABC):
    @abstractmethod
    async def save(self, habit: Habit) -> None:
        pass

    @abstractmethod
    async def find_by_id(self, habit_id: str, user_id: str) -> Optional[Habit]:
        pass

    @abstractmethod
    async def find_all(self, user_id: str) -> Optional[list[Habit]]:
        pass

    @abstractmethod
    async def update(self, habit: Habit) -> None:
        pass

    @abstractmethod
    async def delete(self, habit_id: str, user_id: str) -> None:
        pass
