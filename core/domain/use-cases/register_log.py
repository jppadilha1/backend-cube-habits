from ..entities import HabitLog
from ..repositories import IHabitLogRepository


class RegisterLog:
    def __init__(self, habit_log_repository: IHabitLogRepository):
        self.habit_log_repository = habit_log_repository

    async def execute(self, id: str, habit_id: str, done_at: str) -> None:
        habit_log = HabitLog(id=id, habit_id=habit_id, done_at=done_at)

        await self.habit_log_repository.save(habit_log)
