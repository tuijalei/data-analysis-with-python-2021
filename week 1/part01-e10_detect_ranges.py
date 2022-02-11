
def detect_ranges(L):
    # sort
    L = sorted(L)

    # find differences of increalsing values
    diff = [j-i for i, j in zip(L[:-1], L[1:])]
    diff.insert(0, 0)

    # get pos in diff list    
    ind = [i for i,v in enumerate(diff) if v >= 2]
    ind.insert(0, 0)
    
    # group elements together
    groups = [L[i:j] for i,j in zip(ind, ind[1:]+[None])]

    # obtain desired ranges
    ranges = [(i[0],i[-1]+1) if len(i)>1 else i[0] for i in groups]
    return ranges

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
