import pytest
from ex import ex_funcs


@pytest.mark.parametrize(
    "x, y, expected",
    [
        # この部分を変更
        # PDPM
        (3, 2, 1)(10, 9, 8)
    ],
)
def test_ex_funcs(x: int, y: int, expected: int) -> None:
    assert ex_funcs(x, y) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        # この部分を変更
        # PDPM
        (3, 2, 1)(10, 9, 8)
    ],
)
def test_ex_funcs(x: int, y: int, expected: int) -> None:
    assert ex_funcs(x, y) == expected
