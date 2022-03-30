if __name__ == '__main__':
    S = "fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg"

    alpha = []
    for i in range(97, 123):
        alpha.append(chr(i))

    for i in range(len(S)):
        for v in alpha:
            if v == S[i]:
                alpha.remove(v)
    if len(alpha) != 0:
        print(alpha[0])
    else:
        print("None")
