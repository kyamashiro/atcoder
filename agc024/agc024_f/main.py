#!/usr/bin/env python3
# from typing import *


# def solve(N: int, K: int, X: List[str]) -> Any:
def solve(N, K, X):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, K = map(int, input().split())
    X = [None for _ in range(N + 1)]
    for i in range(N + 1):
        X[i] = input()
    ans = solve(N, K, X)
    print(ans)  # TODO: edit here


if __name__ == '__main__':
    main()