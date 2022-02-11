
import numpy as np

# rely on broadcasting, the np.arange function, reshaping and vectorized operators
def multiplication_table(n):
    a = np.arange(0,n)
    b = a.reshape(n, 1)
    print(a)
    print(b)

    a_br, b_br = np.broadcast_arrays(a, b)
    print(a_br)
    print(b_br)

    return a_br * b_br

def main():
    print(multiplication_table(4))
    #[[0 0 0 0]
    #[0 1 2 3]
    #[0 2 4 6]
    #[0 3 6 9]]

if __name__ == "__main__":
    main()
