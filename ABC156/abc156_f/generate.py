#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    k = random.randint(1, 1000)  # TODO: edit here
    d = [None for _ in range(k)]
    q = random.randint(1, 1000)  # TODO: edit here
    n = [None for _ in range(q)]
    x = [None for _ in range(q)]
    m = [None for _ in range(q)]
    for i in range(k):
        d[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    for i in range(q):
        n[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        x[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        m[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(k, q)
    print(*[d[i] for i in range(k)])
    for i in range(q):
        print(n[i], x[i], m[i])


if __name__ == "__main__":
    main()
