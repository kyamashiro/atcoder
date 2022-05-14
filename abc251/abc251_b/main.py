#!/usr/bin/env python3
# from typing import *


# def solve(N: int, W: int, A: List[int]) -> int:
import itertools


def solve(N, W, A):
    cnt = 0
    arr = set()
    for i in itertools.combinations(A, 1):
        arr.add(sum(i))
    for i in itertools.combinations(A, 2):
        arr.add(sum(i))
    for i in itertools.combinations(A, 3):
        arr.add(sum(i))

    for v in arr:
        if v <= W:
            cnt += 1

    return cnt


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    W = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, W, A)
    print(a)


if __name__ == '__main__':
    main()
