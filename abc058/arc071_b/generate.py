#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n = random.randint(1, 1000)  # TODO: edit here
    x = [None for _ in range(n)]
    m = random.randint(1, 1000)  # TODO: edit here
    y = [None for _ in range(m)]
    for i in range(n):
        x[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    for i in range(m):
        y[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(n, m)
    print(*[x[i] for i in range(n)])
    print(*[y[i] for i in range(m)])


if __name__ == "__main__":
    main()
