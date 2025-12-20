from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.domain.entities import Habit as HabitEntity
from core.domain.repositories import IHabitRepository
from core.domain.value_objects import Description
from core.infra.orm.user_habits import UserHabit as HabitModel


class HabitRepository(IHabitRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, habit: HabitEntity) -> None:
        habit_model = HabitModel(
            id=habit.id,
            user_id=habit.user_id,
            description=habit.description.value,
            created_at=habit.created_at,
            updated_at=habit.updated_at,
        )
        self.session.add(habit_model)
        await self.session.commit()

    async def find_by_id(self, habit_id: str, user_id: str) -> Optional[HabitEntity]:
        result = await self.session.execute(
            select(HabitModel).where(
                HabitModel.id == habit_id, HabitModel.user_id == user_id
            )
        )
        habit_model = result.scalar_one_or_none()

        if habit_model:
            return HabitEntity(
                id=habit_model.id,
                user_id=habit_model.user_id,
                description=Description(habit_model.description),
                created_at=habit_model.created_at,
                updated_at=habit_model.updated_at,
            )
        return None

    async def find_all(self, user_id: str) -> Optional[list[HabitEntity]]:
        result = await self.session.execute(
            select(HabitModel).where(HabitModel.user_id == user_id)
        )
        habit_models = result.scalars().all()

        if not habit_models:
            return None

        return [
            HabitEntity(
                id=model.id,
                user_id=model.user_id,
                description=Description(model.description),
                created_at=model.created_at,
                updated_at=model.updated_at,
            )
            for model in habit_models
        ]

    async def update(self, habit: HabitEntity) -> None:
        result = await self.session.execute(
            select(HabitModel).where(
                HabitModel.id == habit.id, HabitModel.user_id == habit.user_id
            )
        )
        habit_model = result.scalar_one_or_none()

        if habit_model:
            habit_model.description = habit.description.value
            habit_model.updated_at = habit.updated_at
            await self.session.commit()

    async def delete(self, habit_id: str, user_id: str) -> None:
        result = await self.session.execute(
            select(HabitModel).where(
                HabitModel.id == habit_id, HabitModel.user_id == user_id
            )
        )
        habit_model = result.scalar_one_or_none()

        if habit_model:
            await self.session.delete(habit_model)
            await self.session.commit()
