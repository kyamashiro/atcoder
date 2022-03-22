#!/usr/bin/env python3
# from typing import *


# def solve(N: int, A: List[int]) -> List[str]:
def solve(N, A):
    S = []
    for i, v in enumerate(A):
        S.append((v, i + 1))
    S.sort()
    # print(*[j for i, j in S])
    tes = ["a", "b"]


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    solve(N, A)


if __name__ == '__main__':
    main()
