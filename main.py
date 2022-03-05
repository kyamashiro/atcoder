from line_profiler import LineProfiler

profile = LineProfiler()

YES = 'Yes'
NO = 'No'


@profile
def is_sequence(N, S):
    # 6つの連続したマスが存在するかどうか判定する
    horizontal = 0
    vertical = 0
    right_diagonal = 0
    left_diagonal = 0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                # 横の6マスの中に黒のマスが4つ存在するか
                if (S[i][j + k] == "#"):
                    horizontal += 1
                else:
                    # 連続しなかった場合は0にリセットする
                    horizontal = 0

                # 縦の6マスの中に黒のマスが4つ存在するか
                if (S[j + k][i] == "#"):
                    vertical += 1
                else:
                    # 連続しなかった場合は0にリセットする
                    vertical = 0

                # 右斜めの6マスの中に黒のマスが4つ存在するか
                if (S[i + k][j + k] == "#"):
                    right_diagonal += 1
                else:
                    # 連続しなかった場合は0にリセットする
                    right_diagonal = 0

                # 左斜めの6マスの中に黒のマスが4つ存在するか
                if (S[i][j + k] == "#"):
                    left_diagonal += 1
                else:
                    # 連続しなかった場合は0にリセットする
                    left_diagonal = 0
                # 4つ以上連続した場合は2つ埋めて6つ以上になるのでYESを出力する
                if (3 < horizontal or 3 < vertical or 3 < right_diagonal or 3 < left_diagonal):
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
