# tests/test_extra.py
from main import quick_sort


def test_quick_sort_already_sorted():
    assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
