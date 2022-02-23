
import numpy as np
import matplotlib.pyplot as plt

# returns coordinate pair (center_y, center_x) of the image center
def center(a):
    x = (a.shape[0]-1)/2
    y = (a.shape[1]-1)/2
    return (x, y)   # note the order: (center_y, center_x)

# returns for image with width w and height h an array with shape (h,w)
# where the number at index (i,j) gives the euclidean distance from the point (i,j) to the center of the image
def radial_distance(a):
    cent_point = center(a)
    euc_ds = [np.linalg.norm((i-cent_point[0], j-cent_point[1])) for i in range(a.shape[0]) for j in range(a.shape[1])]
    dists = np.array(euc_ds).reshape((a.shape[0], a.shape[1]))
    return dists

# returns a copy of the array a with its elements scaled to be in the range [tmin,tmax]
def scale(a, tmin=0.0, tmax=1.0):
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

# returns an array with same height and width filled with values between 0.0 and 1.0.
def radial_mask(a):
    return scale(1 - radial_distance(a))

# returns the image multiplied by its radial mask.
def radial_fade(a):
    return a * radial_mask(a)[:,:, np.newaxis]

def main():
    image = plt.imread("src/painting.png").copy()
    fig, ax = plt.subplots(1,3)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()

if __name__ == "__main__":
    main()
