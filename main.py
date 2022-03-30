if __name__ == '__main__':
    S = "different"

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] == S[j]:
                print("no")
                exit()
    print("yes")
