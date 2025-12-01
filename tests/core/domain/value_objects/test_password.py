import pytest

from core.domain.value_objects.password import Password


def test_should_create_a_valid_password():
    password = Password("Senhamegasegura#123")
    assert password.value == "Senhamegasegura#123"


def test_should_raise_error_when_password_is_too_short():
    with pytest.raises(ValueError, match="Password must contain at least 8 characters"):
        Password("Abc#1")


def test_should_raise_error_when_password_has_no_uppercase():
    with pytest.raises(
        ValueError, match="Password must contain at least one uppercase letter"
    ):
        Password("senhasegura#123")


def test_should_raise_error_when_password_has_no_number():
    with pytest.raises(ValueError, match="Password must contain at least a number"):
        Password("Senhasegura#")


def test_should_raise_error_when_password_has_no_special_character():
    with pytest.raises(
        ValueError, match="Password must contain at least a special case"
    ):
        Password("Senhasegura123")
