
import math
import numpy as np

def solve_quadratic(a, b, c):
    discr = (b ** 2) - (4*a*c)
    sol1 = (-b-math.sqrt(discr))/(2*a)
    sol2 = (-b+math.sqrt(discr))/(2*a)

    return (sol1, sol2)


def main():
    pass
    print(solve_quadratic(1,-3,2))

if __name__ == "__main__":
    main()
