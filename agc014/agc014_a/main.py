#!/usr/bin/env python3
# from typing import *

def is_even(N):
    return N % 2 == 0


def is_odd(N):
    return N % 2 != 0


# def solve(A: int, B: int, C: int) -> int:
def solve(A, B, C):
    cnt = 0
    while True:
        # print(f"A:{A} B:{B} C:{C}")
        if is_odd(A) or is_odd(B) or is_odd(C):
            break
        if A == B == C:
            cnt = -1
            break

        A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2
        cnt += 1
    return cnt


def main():
    A, B, C = map(int, input().split())
    a = solve(A, B, C)
    print(a)


if __name__ == '__main__':
    main()
