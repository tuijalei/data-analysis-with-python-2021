from matplotlib.pyplot import axes
import numpy as np

def get_rows(a):
    result = []

    for i in range(len(a)):
        result.append(a[i])

    #print(result)
    return result

def get_columns(a):
    result = []
    a = a.T

    for i in range(len(a)):
        result.append(a[i])
    return result

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
