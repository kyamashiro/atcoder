#!/usr/bin/env python3
# from typing import *


# def solve(N: int) -> str:
import math


def solve(N):
    X = math.floor(N / 1.08)
    if math.floor(X * 1.08) == N:
        return X
    elif math.floor((X + 1) * 1.08) == N:
        return X + 1
    elif math.floor((X - 1) * 1.08) == N:
        return X - 1
    else:
        return ":("


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
