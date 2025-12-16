from core.domain.use_cases import (
    CreateHabit,
    FindHabits,
    UpdateHabit,
    DeleteHabit,
    FindAllLogs,  
    RegisterLog,
    LoginUser,
    RegisterUser,
)
from core.factories.use_case_factory import UseCaseFactory
from core.infra.mocks import (
    MockHabitRepository,
    MockHabitLogRepository,
    MockUserRepository,
)



def test_should_create_use_case_with_internal_mocks():
    factory = UseCaseFactory()
    
    register_user_use_case = factory.create_register_user()
    
    assert isinstance(register_user_use_case, RegisterUser)
    assert isinstance(register_user_use_case.user_repository, MockUserRepository)


def test_should_create_use_case_with_external_mocks():
    habit_repo = MockHabitRepository()
    habit_log_repo = MockHabitLogRepository()
    
    factory = UseCaseFactory(
        habit_repository=habit_repo,
        habit_log_repository=habit_log_repo,
    )
    
    create_habit_use_case = factory.create_create_habit()
    register_log_use_case = factory.create_register_log()
    
    assert isinstance(create_habit_use_case, CreateHabit)
    assert isinstance(register_log_use_case, RegisterLog)
    
    # Check if the exact same instance is used
    assert create_habit_use_case.habit_repository is habit_repo
    assert register_log_use_case.habit_log_repository is habit_log_repo
    
    # Check that the non-provided repo is a new mock instance
    assert isinstance(create_habit_use_case.habit_repository, MockHabitRepository)
    assert isinstance(register_log_use_case.habit_log_repository, MockHabitLogRepository)