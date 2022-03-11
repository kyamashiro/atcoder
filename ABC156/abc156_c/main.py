#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: List[int]) -> int:
def solve(N, X):
    results = []
    for P in range(100):
        total = 0
        for xi in range(N):
            total += (X[xi] - P) ** 2
        results.append(total)
    return min(results)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = [None for _ in range(N)]
    for i in range(N):
        X[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X)
    print(a)


if __name__ == '__main__':
    main()
