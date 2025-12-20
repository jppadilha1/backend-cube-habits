from typing import Optional

from core.domain.repositories import (
    IHabitLogRepository,
    IHabitRepository,
    IUserRepository,
)
from core.domain.use_cases import (
    CreateHabit,
    DeleteHabit,
    FindAllLogs,
    FindHabits,
    LoginUser,
    RegisterLog,
    RegisterUser,
    UpdateHabit,
)
from core.infra.mocks import (
    MockHabitLogRepository,
    MockHabitRepository,
    MockUserRepository,
)


class UseCaseFactory:
    def __init__(
        self,
        habit_repository: Optional[IHabitRepository] = None,
        habit_log_repository: Optional[IHabitLogRepository] = None,
        user_repository: Optional[IUserRepository] = None,
    ):
        self.habit_repository = habit_repository or MockHabitRepository()
        self.habit_log_repository = habit_log_repository or MockHabitLogRepository()
        self.user_repository = user_repository or MockUserRepository.get_instance()

    # Habit Use Cases
    def create_create_habit(self) -> CreateHabit:
        return CreateHabit(habit_repository=self.habit_repository)

    def create_find_habits(self) -> FindHabits:
        return FindHabits(habit_repository=self.habit_repository)

    def create_update_habit(self) -> UpdateHabit:
        return UpdateHabit(habit_repository=self.habit_repository)

    def create_delete_habit(self) -> DeleteHabit:
        return DeleteHabit(habit_repository=self.habit_repository)

    # Habit Log Use Cases
    def create_find_all_logs(self) -> FindAllLogs:
        return FindAllLogs(habit_log_repository=self.habit_log_repository)

    def create_register_log(self) -> RegisterLog:
        return RegisterLog(habit_log_repository=self.habit_log_repository)

    # User Use Cases
    def create_register_user(self) -> RegisterUser:
        return RegisterUser(user_repository=self.user_repository)

    def create_login_user(self) -> LoginUser:
        return LoginUser(user_repository=self.user_repository)
    
    def create_find_user_by_email(self) -> 
