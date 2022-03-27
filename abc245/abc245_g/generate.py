#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 1000)  # TODO: edit here
    A = [None for _ in range(N)]
    M = random.randint(1, 1000)  # TODO: edit here
    U = [None for _ in range(M)]
    V = [None for _ in range(M)]
    C = [None for _ in range(M)]
    K = random.randint(1, 10 ** 9)  # TODO: edit here
    L = random.randint(1, 1000)  # TODO: edit here
    B = [None for _ in range(L)]
    for i in range(N):
        A[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    for i in range(L):
        B[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    for i in range(M):
        U[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        V[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        C[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(N, M, K, L)
    print(*[A[i] for i in range(N)])
    print(*[B[i] for i in range(L)])
    for i in range(M):
        print(U[i], V[i], C[i])


if __name__ == "__main__":
    main()
