# tests/test_main.py
import pytest

from main import quick_sort


@pytest.mark.parametrize(
    "data, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 3, 8, 3, 2, 7, 1, 0], [0, 1, 2, 3, 3, 5, 7, 8]),
        (["b", "a", "c"], ["a", "b", "c"]),
    ],
)
def test_quick_sort(data, expected):
    assert quick_sort(data) == expected


def test_quick_sort_does_not_mutate_input():
    data = [3, 2, 1]
    _ = quick_sort(data)
    assert data == [3, 2, 1]
