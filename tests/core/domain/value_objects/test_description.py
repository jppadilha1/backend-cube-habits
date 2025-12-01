import pytest

from core.domain.value_objects.description import Description


def test_should_create_a_valid_username():
    description = Description("Ir à academia 3x por semana")
    assert description.value == "Ir à academia 3x por semana"
    assert len(description.value) >= 20


def test_should_raise_error_too_short():
    with pytest.raises(
        ValueError, match="Description must contain at least 20 characteres"
    ):
        Description("ler 1 pag")
