import numpy as np

    # return array that contains rows from <a> which have the value in the 2nd largest column
    # larger than in the 2nd last column
    # for example for array
    #   [[8 9 3 8 8]
    #   [0 5 3 9 9]
    #   [5 7 6 0 4]
    #   [7 8 1 6 2]
    #   [2 1 3 5 8]]
    # return
    #   [[8 9 3 8 8]
    #   [5 7 6 0 4]
    #   [7 8 1 6 2]

def column_comparison(a):
    return a[a[:, 1] > a[:, -2]]
    
def main():
    pass
    a = np.array([[8, 9, 3, 8, 8],
                  [0, 5, 3, 9, 9],
                  [5, 7, 6, 0, 4],
                  [7, 8, 1, 6, 2],
                  [2, 1, 3, 5, 8]])
    print(column_comparison(a))

if __name__ == "__main__":
    main()
