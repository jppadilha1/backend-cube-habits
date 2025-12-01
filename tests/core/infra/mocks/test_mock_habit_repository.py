from datetime import datetime

import pytest

from core.domain.entities import Habit
from core.domain.value_objects import Description
from core.infra.mocks.mock_habit_repository import MockHabitRepository


class TestMockHabitRepository:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.habit_repository = MockHabitRepository()

    @pytest.mark.asyncio
    async def test_should_create_habit_correctly(self):
        habit = Habit(
            "1",
            "1",
            Description("Jogar bola 10h por semana"),
            datetime.now(),
            datetime.now(),
        )

        # Não deve lançar exceção ao salvar
        await self.habit_repository.save(habit)

        habit_data = await self.habit_repository.find_by_id("1", "1")
        assert habit_data is not None
        assert isinstance(habit_data, Habit)
