from ..entities import Habit
from ..repositories import IHabitRepository


class FindHabits:
    def __init__(self, habit_repository: IHabitRepository):
        self.habit_repository = habit_repository

    async def execute(self, user_id: str) -> list[Habit]:
        habits = await self.habit_repository.find_all(user_id)

        if not habits:
            raise ValueError("Habits not found")

        return habits
