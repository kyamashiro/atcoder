if __name__ == '__main__':
    A, B = map(int, "1 2".split())
    S = "7444"
    if len(S) == A + B + 1 and S[A] == "-" and S.count("-") == 1:
        print("Yes")
    else:
        print("No")
