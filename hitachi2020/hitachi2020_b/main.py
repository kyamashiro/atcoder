#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int, M: int, a: List[int], b: List[int], x: List[int], y: List[int], c: List[int]) -> int:
def solve(A, B, M, a, b, x, y, c):
    latest_a = min(a)
    latest_b = min(b)

    mins = []
    # 割引券なしの最安値
    mins.append(latest_a + latest_b)
    for i in range(M):
        price = a[x[i] - 1] + b[y[i] - 1] - c[i]
        mins.append(price)

    return min(mins)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    A = int(next(tokens))
    B = int(next(tokens))
    M = int(next(tokens))
    a = [None for _ in range(A)]
    b = [None for _ in range(B)]
    x = [None for _ in range(M)]
    y = [None for _ in range(M)]
    c = [None for _ in range(M)]
    for i in range(A):
        a[i] = int(next(tokens))
    for i in range(B):
        b[i] = int(next(tokens))
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        c[i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(A, B, M, a, b, x, y, c)
    print(a1)


if __name__ == '__main__':
    main()
