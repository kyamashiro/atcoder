def main():
    N = 1
    max = 0
    ans = 1
    for i in range(1, N + 1):
        tmp = i
        cnt = 0
        while True:
            if tmp % 2 == 0:
                tmp = tmp / 2
                cnt += 1
                if max < cnt:
                    max = cnt
                    ans = i
            else:
                break
    print(ans)


if __name__ == '__main__':
    main()
