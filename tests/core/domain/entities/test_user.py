from core.domain.entities.user import User
from core.domain.value_objects import Email, Password, Username


def test_should_create_a_valid_user():
    user_test = User(
        id="1",
        username=Username("UserTest"),
        email=Email("test@gmail.com"),
        password=Password("Senhasegura@123"),
    )

    assert user_test.id == "1"
    assert user_test.username.value == "UserTest"
    assert user_test.email.value == "test@gmail.com"
    assert user_test.password.value == "Senhasegura@123"
