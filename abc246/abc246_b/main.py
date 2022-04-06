#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int) -> Tuple[float, float]:
import math


def solve(A, B):
    l = math.sqrt((0 - A) ** 2 + (0 - B) ** 2)
    return A / l, B / l


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B = map(int, input().split())
    c, d = solve(A, B)
    print(c, d)


if __name__ == '__main__':
    main()