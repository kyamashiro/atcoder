#!/usr/bin/env python3
# from typing import *


# def solve(S: str) -> str:
def solve(S):
    ans = "0"
    for i in range(len(S) - 1):
        ans += S[i]
    print(ans)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)


if __name__ == '__main__':
    main()
