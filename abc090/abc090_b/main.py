#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int) -> int:
def solve(A, B):
    cnt = 0
    for n in range(A, B + 1):
        s = list(str(n))
        N = len(s)
        cnt += 1
        for i in range(0, N // 2):
            if s[i] != s[N - 1 - i]:
                cnt -= 1
                break

    return cnt


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B = map(int, input().split())
    a = solve(A, B)
    print(a)


if __name__ == '__main__':
    main()
