#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int, K: int) -> int:
def solve(A, B, K):
    for i in range(10 ** 9):
        if B <= A:
            return i
        A = A * K


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B, K = map(int, input().split())
    a = solve(A, B, K)
    print(a)


if __name__ == '__main__':
    main()
