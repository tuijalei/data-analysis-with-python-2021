
import numpy as np

# gets the coefficients of two lines as parameters
# returns the point where the two lines meet
def meeting_lines(a1, b1, a2, b2):
    
    # matrix form: A * X = B
    # A has shape (n,m) , x unknown shape (m,1) and b shape (n,1)
    A = np.array([[a1, -1], [a2, -1]]) 
    B = -np.array([b1, b2]) 
    
    return np.linalg.solve(A, B)

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
