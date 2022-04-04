def solve(N):
    def f(a, b):
        return (a ** 3) + ((a ** 2) * b) + (a * (b ** 2)) + (b ** 3)

    def is_ok(val):
        return N <= val

    ans = float("INF")

    # aを固定してbを二分探索で見つける
    for a in range(10 ** 6):
        ok = 10 ** 6
        ng = -1
        # 二分探索
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2  # 平均(小数切り捨て)
            # print(f"a:{a} ok:{ok} ng:{ng} mid:{mid} is_ok:{is_ok(f(a, mid))}")
            # N以上になるかどうか
            if is_ok(f(a, mid)):
                ok = mid
            else:
                ng = mid
        ans = min(ans, f(a, ok))
    return ans


if __name__ == '__main__':
    N = int(input())

    ans = solve(N)
    print(ans)
