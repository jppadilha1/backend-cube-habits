from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.domain.entities import HabitLog as HabitLogEntity
from core.domain.repositories import IHabitLogRepository
from core.infra.orm.habits_logs import HabitLog as HabitLogModel


class HabitLogRepository(IHabitLogRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, habit_log: HabitLogEntity) -> None:
        habit_log_model = HabitLogModel(
            id=habit_log.id,
            habit_id=habit_log.habit_id,
            done_at=habit_log.done_at,
        )
        self.session.add(habit_log_model)
        await self.session.commit()

    async def find_all(self, habit_id: str) -> Optional[list[HabitLogEntity]]:
        result = await self.session.execute(
            select(HabitLogModel).where(HabitLogModel.habit_id == habit_id)
        )
        habit_log_models = result.scalars().all()

        if not habit_log_models:
            return None

        return [
            HabitLogEntity(
                id=model.id,
                habit_id=model.habit_id,
                done_at=model.done_at,
            )
            for model in habit_log_models
        ]
