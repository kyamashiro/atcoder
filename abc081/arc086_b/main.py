#!/usr/bin/env python3
# from typing import *


# def solve(N: int, a: List[int]) -> Tuple[str, List[str], List[str]]:
def solve(N, a):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    a = [None for _ in range(N)]
    for i in range(N):
        a[i] = int(next(tokens))
    assert next(tokens, None) is None
    n, a1, b = solve(N, a)
    print(n)
    for i in range(n):
        print(a1[i], b[i])


if __name__ == '__main__':
    main()
