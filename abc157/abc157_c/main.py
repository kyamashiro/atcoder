#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, s: List[int], c: List[int]) -> int:
def solve(N, M, s, c):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    s = [None for _ in range(M)]
    c = [None for _ in range(M)]
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    a = solve(N, M, s, c)
    print(a)


if __name__ == '__main__':
    main()
