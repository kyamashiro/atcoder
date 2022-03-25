import itertools


# def solve(N: int, P: List[int], Q: List[int]) -> int:
def solve(N, P, Q):
    a = 0
    b = 0
    for i, v in enumerate(list(itertools.permutations(range(1, N + 1)))):
        if list(v) == P:
            a = i
        if list(v) == Q:
            b = i
    return abs(a - b)


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    P = [None for _ in range(N)]
    Q = [None for _ in range(N)]
    for i in range(N):
        P[i] = int(next(tokens))
    for i in range(N):
        Q[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, P, Q)
    print(a)


if __name__ == '__main__':
    main()
