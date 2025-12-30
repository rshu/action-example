# main.py
from __future__ import annotations
from typing import Iterable, List, TypeVar

T = TypeVar("T")


def quick_sort(items: Iterable[T]) -> List[T]:
    arr = list(items)
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
