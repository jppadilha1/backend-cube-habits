from core.domain.entities.habit import Habit
from core.domain.value_objects.description import Description


def test_should_create_a_valid_habit():
    habit_test = Habit(
        id="1",
        user_id="123",
        description=Description("Beber 2 litros de água por dia"),
        created_at="2024-01-15T10:00:00",
        updated_at="2024-01-15T10:00:00",
    )

    assert habit_test.id == "1"
    assert habit_test.user_id == "123"
    assert habit_test.description.value == "Beber 2 litros de água por dia"
    assert habit_test.created_at == "2024-01-15T10:00:00"
    assert habit_test.updated_at == "2024-01-15T10:00:00"
