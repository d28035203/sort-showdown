#!/usr/bin/env python3
"""sort-showdown — compare classic sorts on the same input."""
from __future__ import annotations

import argparse
import random
import time
from typing import Callable, List, Tuple


def bubble(a: List[int]) -> Tuple[List[int], int]:
    data = a[:]
    comps = 0
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data, comps


def insertion(a: List[int]) -> Tuple[List[int], int]:
    data = a[:]
    comps = 0
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            else:
                break
        data[j + 1] = key
    return data, comps


def quicksort(a: List[int]) -> Tuple[List[int], int]:
    data = a[:]
    comps = [0]

    def _qs(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        pivot = data[hi]
        i = lo
        for j in range(lo, hi):
            comps[0] += 1
            if data[j] <= pivot:
                data[i], data[j] = data[j], data[i]
                i += 1
        data[i], data[hi] = data[hi], data[i]
        _qs(lo, i - 1)
        _qs(i + 1, hi)

    _qs(0, len(data) - 1)
    return data, comps[0]


def mergesort(a: List[int]) -> Tuple[List[int], int]:
    comps = [0]

    def merge(left: List[int], right: List[int]) -> List[int]:
        out: List[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            comps[0] += 1
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        out.extend(left[i:])
        out.extend(right[j:])
        return out

    def sort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        return merge(sort(arr[:mid]), sort(arr[mid:]))

    return sort(a[:]), comps[0]


ALGOS: dict[str, Callable[[List[int]], Tuple[List[int], int]]] = {
    "bubble": bubble,
    "insertion": insertion,
    "quick": quicksort,
    "merge": mergesort,
}


def main() -> int:
    p = argparse.ArgumentParser(description="Compare sorting algorithms")
    p.add_argument("-n", type=int, default=20, help="array size")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--sorted", action="store_true", help="already-sorted input")
    p.add_argument("--reverse", action="store_true", help="reverse-sorted input")
    args = p.parse_args()

    random.seed(args.seed)
    if args.sorted:
        data = list(range(args.n))
    elif args.reverse:
        data = list(range(args.n, 0, -1))
    else:
        data = [random.randint(0, args.n * 10) for _ in range(args.n)]

    print(f"n={args.n} seed={args.seed}")
    print(f"input: {data if args.n <= 30 else data[:15] + ['...']}")
    print(f"{'algo':<10} {'ms':>10} {'comps':>10} ok")
    reference = sorted(data)
    for name, fn in ALGOS.items():
        t0 = time.perf_counter()
        out, comps = fn(data)
        ms = (time.perf_counter() - t0) * 1000
        ok = out == reference
        print(f"{name:<10} {ms:10.3f} {comps:10d} {'yes' if ok else 'NO'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
