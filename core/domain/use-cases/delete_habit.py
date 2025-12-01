from ..repositories import IHabitRepository


class DeleteHabit:
    def __init__(self, habit_repository: IHabitRepository):
        self.habit_repository = habit_repository

    async def execute(self, habit_id: str, user_id: str) -> None:
        await self.habit_repository.delete(habit_id, user_id)
