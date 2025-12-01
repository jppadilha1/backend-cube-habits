import pytest

from core.domain.value_objects.username import Username


def test_should_create_a_valid_username():
    username = Username("Fulano")
    assert username.value == "Fulano"


def test_should_raise_error_too_short():
    with pytest.raises(
        ValueError, match="Username must contain at least 5 characteres"
    ):
        Username("KKK")
