#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, P: List[int], Y: List[int]) -> List[str]:
def solve(N, M, P, Y):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    P = [None for _ in range(M)]
    Y = [None for _ in range(M)]
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    ans = solve(N, M, P, Y)
    for i in range(M):
        print(ans[i])


if __name__ == '__main__':
    main()
