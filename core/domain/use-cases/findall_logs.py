from ..entities import HabitLog
from ..repositories import IHabitLogRepository


class FindAllLogs:
    def __init__(self, habit_log_repository: IHabitLogRepository):
        self.habit_log_repository = habit_log_repository

    async def execute(self, habit_id: str) -> list[HabitLog]:
        all_logs_by_id = await self.habit_log_repository.find_all(habit_id)

        return all_logs_by_id if all_logs_by_id else []
