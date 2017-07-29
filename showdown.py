#!/usr/bin/env python3
"""sort-showdown — compare basic sorting algorithms."""
from __future__ import print_function
import random, time, copy

def bubble(a):
    a = list(a)
    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return a, swaps

def insertion(a):
    a = list(a)
    moves = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            moves += 1
        a[j + 1] = key
    return a, moves

def quicksort(a):
    a = list(a)
    def qs(lo, hi):
        if lo >= hi:
            return
        pivot = a[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        qs(lo, j)
        qs(i, hi)
    qs(0, len(a) - 1)
    return a

def main():
    data = [random.randint(0, 99) for _ in range(12)]
    print("input:", data)
    for name, fn in [("bubble", bubble), ("insertion", insertion)]:
        out, metric = fn(data)
        print("%-10s -> %s  metric=%d" % (name, out, metric))
    print("%-10s -> %s" % ("quicksort", quicksort(data)))

if __name__ == "__main__":
    main()
