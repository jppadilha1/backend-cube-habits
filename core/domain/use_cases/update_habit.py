from datetime import datetime

from ..entities import Habit
from ..repositories import IHabitRepository


class UpdateHabit:
    def __init__(self, habit_repository: IHabitRepository):
        self.habit_repository = habit_repository

    async def execute(self, habit: Habit) -> Habit:
        saved_habit = await self.habit_repository.find_by_id(habit.id, habit.user_id)

        if not saved_habit:
            raise ValueError("Habit not found")

        new_description = (
            habit.description if habit.description else saved_habit.description
        )
        new_updated_at = datetime.now().isoformat()

        updated = Habit(
            id=habit.id,
            user_id=habit.user_id,
            description=new_description,
            created_at=habit.created_at,
            updated_at=new_updated_at,
        )

        await self.habit_repository.update(updated)

        return updated
