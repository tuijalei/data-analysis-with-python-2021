
def merge(L1, L2):
    size_1 = len(L1)
    size_2 = len(L2)
    list = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if L1[i] < L2[j]:
            list.append(L1[i])
            i += 1

        else:
            list.append(L2[j])
            j += 1

    return list + L1[i:] + L2[j:]

def main():
    pass
    L1 = [1,2,7]
    L2 = [3,4,9]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
