#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(N: int, W: List[str]) -> str:
def solve(N, W):
    if len(W) != len(set(W)):
        return NO

    for i in range(N - 1):
        if W[i][-1] != W[i + 1][0]:
            return NO

    return YES


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    W = [None for _ in range(N)]
    for i in range(N):
        W[i] = input()
    a = solve(N, W)
    print(a)


if __name__ == '__main__':
    main()
