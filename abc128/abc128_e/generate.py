#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 1000)  # TODO: edit here
    S = [None for _ in range(N)]
    T = [None for _ in range(N)]
    X = [None for _ in range(N)]
    Q = random.randint(1, 1000)  # TODO: edit here
    D = [None for _ in range(Q)]
    for i in range(N):
        S[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        T[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        X[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    for i in range(Q):
        D[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(N, Q)
    for i in range(N):
        print(S[i], T[i], X[i])
    for i in range(Q):
        print(D[i])


if __name__ == "__main__":
    main()
