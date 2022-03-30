import string

if __name__ == '__main__':
    s = "atcoderregularcontest"
    for i in string.ascii_lowercase:
        if i not in s:
            print(i)
            break
    else:
        print("None")
