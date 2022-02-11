
import numpy as np

def get_row_vectors(a):
    result = []

    for i in range(len(a)):
        #print(a[i])
        result.append(a[[i], :])

    return result

def get_column_vectors(a):
    result = []
    a = a.T
    #parts = np.split(a, (a.shape[0],), axis=1)[0]
    #result.append(parts)
 
    for i in range(len(a)):
        result.append(a[[i], :].reshape(-1,1))

    return result

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (3,5))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))


if __name__ == "__main__":
    main()
