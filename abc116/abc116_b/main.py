#!/usr/bin/env python3
# from typing import *


# def solve(s: int) -> int:
def solve(s):
    l = []
    tmp = s
    l.append(tmp)
    while True:
        if tmp % 2 == 0:
            tmp = tmp // 2
        else:
            tmp = 3 * tmp + 1
        if tmp in l:
            print(len(l) + 1)
            break
        l.append(tmp)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    s = int(input())
    solve(s)


if __name__ == '__main__':
    main()
