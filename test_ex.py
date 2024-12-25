import pytest
from ex import ex_funcs

# コンフリクトを起こす


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (3, 2, 1),
        (3, 3, 0),
        (3, 4, -1),
    ],
)
def test_ex_funcs(x: int, y: int, expected: int) -> None:
    assert ex_funcs(x, y) == expected
