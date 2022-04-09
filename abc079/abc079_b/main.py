#!/usr/bin/env python3
# from typing import *


# def solve(N: int) -> int:
def solve(N):
    L0 = 2
    L1 = 1

    for i in range(1, N):
        L0, L1 = L1, L0 + L1

    return L1


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
