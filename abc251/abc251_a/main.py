#!/usr/bin/env python3
# from typing import *


# def solve(S: str) -> str:
def solve(S):
    if len(S) == 1:
        return S * 6
    if len(S) == 2:
        return S * 3
    if len(S) == 3:
        return S * 2


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
