import pytest
from ex import ex_funcs



@pytest.mark.parametrize(
    "x, y, expected",
    [
        # この部分を変更
        (3,2,1)
    ],
)
def test_ex_funcs(x: int, y: int, expected: int) -> None:
    assert ex_funcs(x, y) == expected
