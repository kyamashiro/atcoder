#!/usr/bin/env python3
# from typing import *


# def solve(a: int, b: int) -> str:
def solve(a, b):
    if a <= 0 <= b:
        return "Zero"

    if 0 < a or 0 < b:
        return "Positive"

    if a < 0 or b < 0:
        if (b - a + 1) % 2 != 0:
            return "Negative"
        else:
            return "Positive"


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a, b = map(int, input().split())
    a1 = solve(a, b)
    print(a1)


if __name__ == '__main__':
    main()
