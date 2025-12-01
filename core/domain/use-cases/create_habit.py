from ..entities import Habit
from ..repositories import IHabitRepository


class CreateHabit:
    def __init__(self, habit_repository: IHabitRepository):
        self.habit_repository = habit_repository

    async def execute(self, habit: Habit) -> None:
        await self.habit_repository.save(habit)
