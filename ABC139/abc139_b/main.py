#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int) -> int:
def solve(A, B):
    # コンセントの数
    outlet = 1
    # 必要な電源タップの個数
    ans = 0
    while outlet < B:
        # 小口を1つ減らす
        outlet -= 1
        outlet += A
        ans += 1
    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B = map(int, input().split())
    a = solve(A, B)
    print(a)


if __name__ == '__main__':
    main()
