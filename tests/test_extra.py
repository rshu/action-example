# tests/test_extra.py
from main import quick_sort


def test_quick_sort_with_duplicates():
    assert quick_sort([2, 2, 1, 1, 3]) == [1, 1, 2, 2, 3]
