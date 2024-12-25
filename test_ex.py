import pytest

from ex import ex_funcs

# PDPM


@pytest.mark.parametrize(
    "x, y, expected",
    [
        # この部分を変更
        # PDPM
        (3, 2, 1),
        (10, 9, 8),
        (11, 11, 11)
    ],
)
def test_ex_funcs(x: int, y: int, expected: int) -> None:
    assert ex_funcs(x, y) == expected


def test_ex_funcs(x: int, y: int, expected: int) -> None:

