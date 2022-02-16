import numpy as np

# two 2-dimensional arrays of shape (n, 2*m)
# returns matrix with the rows which have the sum of the first m elements larger
# than the sum of the last m elements on the row

def first_half_second_half(a):
    halfway = a.shape[1] // 2 # one for double, two for int
    print(halfway)
    first_half = np.sum(a[:, :halfway], axis=1) # axis = 1 for rows
    print(first_half)
    second_half = np.sum(a[:, halfway:], axis=1)
    print(second_half)
    
    return a[first_half > second_half]

def main():
    pass
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
    print(first_half_second_half(a)) # array([[2, 2, 1, 2]]) expected
    

if __name__ == "__main__":
    main()
