
def distinct_characters(L):
    dict_char = {}

    for i in range(0, len(L)):
        dict_char[L[i]] = len(set(L[i]))

    return dict_char

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
