
def find_matching(L, pattern):
    ids = []
    for i, word in enumerate(L):
        print(i, word)
        if pattern in word:
            ids.append(i)
    return ids

def main():
    pass
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
