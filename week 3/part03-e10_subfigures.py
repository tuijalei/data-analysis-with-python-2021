
import numpy as np
import matplotlib.pyplot as plt

# creates a figure that has two subfigures
# gets a two dimensional array a as a parameter
# 
# In the left subfigure draw using the plot method a graph, 
# whose x coordinates are in the first column of a and the y coordinates are in the second column of a.
# 
# In the right subfigure draw using the scatter method a set of points whose x coords are again in the 
# first column of a and whose y coordinates are in the second column of a.
# 
# Additionally, the points should get their color from the third column of a, and size of the point from the fourth column of a
# 
def subfigures(a):
    fig, ax = plt.subplots(1, 2)
    
    ax[0].plot(a[:, 0], a[:, 1]) # line plot
    ax[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3]) # scatter

    plt.show()
    

def main():
    pass
    subfigures(np.array([[1,2,3], [4,3,2], [0.0, 2.0, 1.0], [10, 10, 10]]))

if __name__ == "__main__":
    main()
