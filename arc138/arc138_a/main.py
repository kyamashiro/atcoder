#!/usr/bin/env python3
# from typing import *


# def solve(N: int, K: int, A: List[int]) -> int:
def solve(N, K, A):
    score = sum(A[:K])
    maxArr = sorted(A, reverse=True)[:K]
    maxScore = sum(maxArr)

    if score >= maxScore:
        return -1

    # 並び替え
    cnt = 0
    for i, v in enumerate(A):
        # 最大値の配列に含まれていない場合、移動したときの値を入れる
        if v not in maxArr:
            print(f"val:{v} i:{i} index:{A.index(v)}")
            cnt += A.index(v) - i

    return cnt


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, K, A)
    print(a)


if __name__ == '__main__':
    main()