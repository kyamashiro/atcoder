#!/usr/bin/env python3
# from typing import *


# def solve(N: int, K: int, X: int, A: List[int]) -> int:
def solve(N, K, X, A):
    ans = sum(A)
    rem = K  # クーポンの残り枚数
    Q = sum(x // X for x in A)  # X円引きできる回数
    R = sorted((x % X for x in A), reverse=True)  # X円引きし終わったあとの余りを大きい順に並べる
    ans -= X * min(Q, rem)  # Qとクーポンの枚数の少ない方だけX円引きできる
    rem -= min(Q, rem)  # X円引きに使った分クーポンを減らす
    # 0~remまでの合計
    ans -= sum(R[:rem])  # 大きい順に使う（スライスは配列外参照を起こさないので、remが巨大でも問題ありません）
    print(ans)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    X = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    solve(N, K, X, A)


if __name__ == '__main__':
    main()