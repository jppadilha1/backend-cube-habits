import pytest
from datetime import datetime

from core.domain.entities import HabitLog
from core.infra.mocks.mock_habit_log_repository import MockHabitLogRepository


class TestMockHabitLogRepository:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.habit_log_repository = MockHabitLogRepository()

    @pytest.mark.asyncio
    async def test_should_create_log_correctly(self):
        log = HabitLog("1", "1", datetime.now())

        # Não deve lançar exceção ao salvar
        await self.habit_log_repository.save(log)

        log_data = await self.habit_log_repository.find_all("1")
        assert log_data is not None
        assert len(log_data) > 0
