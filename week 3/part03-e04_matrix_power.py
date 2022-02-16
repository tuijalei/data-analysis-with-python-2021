import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    if n < 0:
        a = np.linalg.inv(a)
        n = n*(-1)
        
    return reduce(lambda x, y: x@y, (a for x in range(n)))

def main():
    a = np.array([[0, 1, 0], [-1, 0, -1]])
    print(matrix_power(a, 2))

if __name__ == "__main__":
    main()
