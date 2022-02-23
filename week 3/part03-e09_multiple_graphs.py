import matplotlib.pyplot as plt

# Make your main function plot the following two graphs in one axes: 
# The first graphs has x coordinates 2,4,6,7 and y coordinates 4,3,5,1.
# The second graph has x coordinates 1,2,3,4 and y coordinates 4,2,3,1.
# Add also a title and some labels for x axis and y axis.
def main():
    pass
    ax = plt.axes
    plt.plot((2,4,6,7), (4,3,5,1))
    plt.plot((1,2,3,4), (4,2,3,1))
    plt.title('title')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    plt.show()

if __name__ == "__main__":
    main()
