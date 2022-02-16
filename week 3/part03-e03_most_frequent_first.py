from collections import Counter
import numpy as np

# a two dimensional array and an index c of a column as parameters
# returns the array whose rows are sorted based on column c: rows ordered that those rows with
# the most frequent element in column c come first and so on

def most_frequent_first(a, c):
    the_c = a[:, c]
    print('the rows are sorted based on the column', the_c)
    unique, count = np.unique(the_c, return_counts=True)
    print('The unique values and counts are\n', dict(zip(unique, count)))

    # 0: 2,    1: 3,    2: 2,    3: 1,    4: 1,    9: 1
    # So first we need the row from indeces 1, 3, 8
    # then from indeces 2, 4, 
    # then 6, 9, then 7, 
    # then 0 and 
    # finally 5

    ordered = unique[count.argsort()][::-1]
    result_arr = np.concatenate([a[a[:, c] == i] for i in ordered])
    
    return result_arr

def main():
    pass
    a = np.array([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
                  [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
                  [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
                  [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
                  [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
                  [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
                  [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
                  [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
                  [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
                  [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]])
    print('Result\n', most_frequent_first(a, -1))
    # Should get
    # [[4 4 8 4 3 7 5 5 0 1]
    # [2 3 8 1 3 3 3 7 0 1]
    # [7 6 8 8 1 6 7 7 8 1]
    # [5 9 3 0 5 0 1 2 4 2]
    # [8 1 1 7 9 9 3 6 7 2]
    # [9 9 0 4 7 3 2 7 2 0]
    # [5 9 8 9 4 3 0 3 5 0]
    # [0 3 5 9 4 4 6 4 4 3]
    # [0 4 5 5 6 8 4 1 4 9]
    # [5 0 3 3 7 9 3 5 2 4]]

if __name__ == "__main__":
    main()
