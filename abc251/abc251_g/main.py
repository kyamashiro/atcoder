#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(N: int, x: List[int], y: List[int], M: int, u: List[int], v: List[int], Q: int, a: List[int], b: List[int]) -> List[str]:
def solve(N, x, y, M, u, v, Q, a, b):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    x = [None for _ in range(N)]
    y = [None for _ in range(N)]
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    M = int(input())
    u = [None for _ in range(M)]
    v = [None for _ in range(M)]
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    Q = int(input())
    a = [None for _ in range(Q)]
    b = [None for _ in range(Q)]
    for i in range(Q):
        a[i], b[i] = map(int, input().split())
    c = solve(N, x, y, M, u, v, Q, a, b)
    for i in range(Q):
        print(c[i])


if __name__ == '__main__':
    main()
