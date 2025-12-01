from core.domain.entities.habit_log import HabitLog


def test_should_create_a_valid_habit_log():
    habit_log_test = HabitLog(id="1", habit_id="456", done_at="2024-01-15T14:30:00")

    assert habit_log_test.id == "1"
    assert habit_log_test.habit_id == "456"
    assert habit_log_test.done_at == "2024-01-15T14:30:00"
