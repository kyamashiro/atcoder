#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 1000)  # TODO: edit here
    a = [None for _ in range(N - 1)]
    b = [None for _ in range(N - 1)]
    for i in range(N - 1):
        a[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        b[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    M = random.randint(1, 1000)  # TODO: edit here
    u = [None for _ in range(M)]
    v = [None for _ in range(M)]
    for i in range(M):
        u[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        v[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(N)
    for i in range(N - 1):
        print(a[i], b[i])
    print(M)
    for i in range(M):
        print(u[i], v[i])


if __name__ == "__main__":
    main()