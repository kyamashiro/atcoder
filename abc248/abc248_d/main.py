#!/usr/bin/env python3
# from typing import *

def is_ok(X, i):
    return i == X


# def solve(n: int, a: List[int]) -> Tuple[str, List[str]]:
def solve(N, A, Q, Query):
    for i in range(Q):
        L, R, X = Query[i][0], Query[i][1], Query[i][2]
        cnt = 0
        l = sorted(list(A[L - 1:R]))

        ok, ng = X, -1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if is_ok(X, mid):
                ok = mid
            else:
                ng = mid

        for v in sorted(list(A[L - 1:R])):
            if v == X:
                cnt += 1
            if X < v:
                break
        print(cnt)


def main():
    N = int(input())  # TODO: edit here
    A = list(map(int, input().split()))  # TODO: edit here
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))
    solve(N, A, Q, Query)


if __name__ == '__main__':
    main()
