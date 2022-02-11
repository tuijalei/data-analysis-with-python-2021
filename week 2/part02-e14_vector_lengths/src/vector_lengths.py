
import numpy as np
import scipy.linalg

def vector_lengths(a):
    dist = np.sqrt(np.sum((a ** 2), axis=1))
    return dist

def main():
    arr = np.array([[1,2,3], [4,5,6]])
    arr_2 = np.array([[5,6,7,8], [12,33,45,69]])
    print(arr)
    dist = vector_lengths(arr)
    print(vector_lengths((arr_2)))
    print(dist)
    pass

if __name__ == "__main__":
    main()
    
