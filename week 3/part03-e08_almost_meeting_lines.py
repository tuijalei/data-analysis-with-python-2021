import numpy as np
from numpy.linalg import solve, lstsq, LinAlgError

# gets the coefficients of two lines as parameters
# returns the meeting point if it exist, otherwise the closes point
def almost_meeting_lines(a1, b1, a2, b2):
    a = np.array([[a1, -1], [a2, -1]])
    b = -np.array([b1, b2])
    
    try:
        point = solve(a,b)
        return point, True
    except LinAlgError:
        point = lstsq(a,b)[0]
        return point, False

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}") # should be -1.000000 1.000000 True

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
