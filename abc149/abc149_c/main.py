#!/usr/bin/env python3
# from typing import *

def isitPrime(k):
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False

    return True


# def solve(X: int) -> int:
def solve(X):
    while True:
        if isitPrime(X):
            return X
        else:
            X += 1


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    X = int(input())
    a = solve(X)
    print(a)


if __name__ == '__main__':
    main()
