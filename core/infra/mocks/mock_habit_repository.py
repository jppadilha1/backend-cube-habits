from typing import Optional

from ...domain.entities import Habit
from ...domain.repositories import IHabitRepository


class MockHabitRepository(IHabitRepository):
    def __init__(self):
        self.habits: list[Habit] = []

    async def save(self, habit: Habit) -> None:
        self.habits.append(habit)

    async def find_by_id(self, habit_id: str, user_id: str) -> Optional[Habit]:
        return next(
            (
                habit
                for habit in self.habits
                if habit.id == habit_id and habit.user_id == user_id
            ),
            None,
        )

    async def find_all(self, user_id: str) -> Optional[list[Habit]]:
        filtered = [habit for habit in self.habits if habit.user_id == user_id]
        return filtered if len(filtered) > 0 else None

    async def update(self, habit: Habit) -> None:
        index = next((i for i, h in enumerate(self.habits) if h.id == habit.id), None)
        if index is not None:
            self.habits[index] = habit

    async def delete(self, habit_id: str, user_id: str) -> None:
        self.habits = [
            habit
            for habit in self.habits
            if not (habit.id == habit_id and habit.user_id == user_id)
        ]

    def reset(self) -> None:
        self.habits = []
