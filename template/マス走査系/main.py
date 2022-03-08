YES = 'Yes'
NO = 'No'


def is_sequence(N, S):
    # (x,y) を始点として (dx,dy) 方向を調べる
    # 問題の条件を満たす列が見つかれば True
    def calc(x, y, dx, dy):
        count = 0
        print("==================================")
        for i in range(6):
            print(f"x:{x} y:{y} dx:{dx} dy:{dy}")
            print(f"S[{x}][{y}]")
            if not (0 <= min(x, y) and max(x, y) < N):
                # マス目からはみ出したら失敗
                return False
            if S[x][y] == '#':
                count += 1
            x += dx
            y += dy
        # 4 個以上黒で塗られていれば True
        return count >= 4

    Dx = [1, 0, 1, 1]
    Dy = [0, 1, 1, -1]
    for x in range(N):
        for y in range(N):
            for dx, dy in zip(Dx, Dy):
                if calc(x, y, dx, dy):
                    return True
    return False


def solve(N, S):
    # 2つのマスを塗りつぶす
    if (is_sequence(N, S)):
        return YES
    return NO


def main():
    stdin = open("in.txt")
    N = int(stdin.readline().rstrip())
    S = []
    for _ in range(N):
        S.append(list(stdin.readline().rstrip()))
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
