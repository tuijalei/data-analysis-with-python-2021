
import numpy as np

# gets the coefficients of three planes as parameters
# returns the point where the planes meet
def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    
    # plane is Ax + By +Cz = 0
    a = np.array([[b1, a1, -1], [b2, a2, -1], [b3, a3, -1]])
    b = -np.array([c1, c2, c3])
    return np.linalg.solve(a,b)

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
