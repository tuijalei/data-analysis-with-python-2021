
def interleave(*lists):
    li = []

    for a in zip(*lists):
        li.extend(a)

    return li
    

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
