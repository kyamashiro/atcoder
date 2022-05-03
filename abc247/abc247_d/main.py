from collections import deque


def solve(n, a):
    q = deque([])
    for arr in a:
        if arr[0] == 1:
            q.append([arr[1], arr[2]])

        if arr[0] == 2:
            # 取り出す玉の数
            output = arr[1]
            # 取り出した数の合計
            total = 0
            while 0 < output:
                tmp = q.popleft()
                # 取り出す玉の数 < 取り出した玉の数が多いとき、余った玉をqueueに戻す
                if output < tmp[1]:
                    # 取り出す玉の数 * 玉の数字
                    total += tmp[0] * output
                    # 余った玉をqueueに戻す
                    q.appendleft([tmp[0], tmp[1] - output])
                    output -= tmp[1]
                # 取り出す玉の数 > 取り出した玉の数が多いとき
                else:
                    total += tmp[0] * tmp[1]
                    output -= tmp[1]
            print(total)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n = int(input())
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    solve(n, a)


if __name__ == '__main__':
    main()