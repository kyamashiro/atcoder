#!/usr/bin/env python3
# from typing import *


# def solve(n: int, S: List[str]) -> Any:
def solve(n, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n = int(input())
    S = [None for _ in range(n)]
    for i in range(n):
        S[i] = input()
    ans = solve(n, S)
    print(ans)  # TODO: edit here


if __name__ == '__main__':
    main()