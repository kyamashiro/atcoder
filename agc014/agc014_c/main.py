#!/usr/bin/env python3
# from typing import *


# def solve(H: str, W: str, K: str, A: List[List[str]]) -> int:
def solve(H, W, K, A):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    H = next(tokens)
    W = next(tokens)
    K = next(tokens)
    A = [[None for _ in range(W)] for _ in range(H + W + 2)]
    for j in range(H + 2):
        for i in range(W):
            A[i + j][i] = next(tokens)
    assert next(tokens, None) is None
    a = solve(H, W, K, A)
    print(a)


if __name__ == '__main__':
    main()