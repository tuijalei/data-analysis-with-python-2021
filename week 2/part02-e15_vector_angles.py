
import numpy as np
import numpy.linalg as la

def vector_angles(X,Y):
    dotProd = np.sum(np.multiply(X,Y))
    x_norm = np.sqrt(np.sum(np.square(X)))
    y_norm = np.sqrt(np.sum(np.square(Y)))
    radians = np.arccos((dotProd / np.multiply(x_norm, y_norm)))
    
    return np.array(radians*180/np.pi)

def main():
    a = np.array([8,6])
    b = np.array([7,9])
    print('result', vector_angles(a, b))

    c = np.array([[1,2,3], [4,5,6]])
    d = np.array([[1,5,9], [5,7,8]])
    print('result', vector_angles(c, d))

    e = np.array([[0,0,1], [-1,1,0]])
    f = np.array([[0,1,0], [1,1,0]])
    print('result', vector_angles(e, f))

if __name__ == "__main__":
    main()
