#!/usr/bin/env python3
# from typing import *


# def solve(N: int, A: List[int]) -> int:
def solve(N, A):
    l = [i for i in range(2001)]

    for n in A:
        if n in l:
            l.remove(n)
    return min(l)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(a)


if __name__ == '__main__':
    main()
