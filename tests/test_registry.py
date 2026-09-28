import pytest

from tools.registry import ToolRegistry


def test_register_and_execute():

    registry = ToolRegistry()

    registry.register(
        "calculator",
        "add",
        lambda a, b: a + b,
    )

    result = registry.execute(
        "calculator",
        "add",
        {"a": 2, "b": 3},
    )

    assert result == 5


def test_unknown_tool():

    registry = ToolRegistry()

    with pytest.raises(ValueError):
        registry.execute(
            "missing",
            "run",
            {},
        )