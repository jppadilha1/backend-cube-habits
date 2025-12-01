import pytest

from core.domain.entities import User
from core.domain.value_objects import Email, Password, Username
from core.infra.mocks.mock_user_repository import MockUserRepository


class TestMockUserRepository:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_repository = MockUserRepository()

    @pytest.mark.asyncio
    async def test_should_not_throw_when_updating_non_existent_user(self):
        user = User(
            id="1",
            username=Username("Romário"),
            email=Email("goat@gmail.com"),
            password=Password("senha$Segura123"),
        )

        # Não deve lançar exceção
        await self.user_repository.update(user)

    @pytest.mark.asyncio
    async def test_should_save_user_correctly(self):
        user = User(
            id="1",
            username=Username("Romário"),
            email=Email("goat@gmail.com"),
            password=Password("senha$Segura123"),
        )

        await self.user_repository.save(user)

        user_data = await self.user_repository.find_by_email("goat@gmail.com")

        assert user_data is not None
        assert isinstance(user_data, User)
        assert user_data.email.value == "goat@gmail.com"
