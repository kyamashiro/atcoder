#!/usr/bin/env python3
# from typing import *


# def solve(N: int) -> List[List[str]]:
def solve(N):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    a = solve(N)
    for j in range(N):
        print(*[a[j][i] for i in range(N)])


if __name__ == '__main__':
    main()
