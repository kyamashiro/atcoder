#!/usr/bin/env python3
# from typing import *


# def solve(N: int, D: int, A: int, X: List[int], H: List[int]) -> int:
def solve(N, D, A, X, H):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, D, A = map(int, input().split())
    X = [None for _ in range(N)]
    H = [None for _ in range(N)]
    for i in range(N):
        X[i], H[i] = map(int, input().split())
    a = solve(N, D, A, X, H)
    print(a)


if __name__ == '__main__':
    main()
