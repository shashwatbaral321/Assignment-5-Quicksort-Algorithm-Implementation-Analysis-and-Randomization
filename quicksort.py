# quicksort.py

import random
import time
import tracemalloc
from typing import List

def deterministic_partition(arr: List[int], low: int, high: int) -> int:
    # Lomuto-style partition but pivot = arr[low]
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # put pivot in place
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def deterministic_quicksort(arr: List[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, p - 1)
        deterministic_quicksort(arr, p + 1, high)
