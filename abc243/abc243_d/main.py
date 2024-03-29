#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, S: str) -> int:
def solve(N, X, S):
    T = []

    for i in range(N):
        # LまたはRの次にUが来る場合は元の場所に戻るだけなので削除してOK
        if S[i] == "U" and len(T) > 0 and (T[-1] == "L" or T[-1] == "R"):
            T.pop()
        else:
            T.append(S[i])

    for t in T:
        # 現在地
        if (t == "U"):
            X = X // 2
        if (t == "L"):
            X = X * 2
        if (t == "R"):
            X = X * 2 + 1

    return X


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, X = map(int, input().split())
    S = input()
    a = solve(N, X, S)
    print(a)


if __name__ == '__main__':
    main()
