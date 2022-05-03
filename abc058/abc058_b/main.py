#!/usr/bin/env python3
# from typing import *


# def solve(O: str, E: str) -> str:
def solve(O, E):
    ans = ""
    for i in range(max(len(O), len(E))):
        if i < len(O):
            ans += O[i]

        if i < len(E):
            ans += E[i]
    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    O = input()
    E = input()
    a = solve(O, E)
    print(a)


if __name__ == '__main__':
    main()
