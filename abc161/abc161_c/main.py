#!/usr/bin/env python3
# from typing import *


# def solve(N: int, K: int) -> int:
def solve(N, K):
    if N % K < abs(N % K - K):
        return N % K
    else:
        return abs(N % K - K)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, K = map(int, input().split())
    a = solve(N, K)
    print(a)


if __name__ == '__main__':
    main()
