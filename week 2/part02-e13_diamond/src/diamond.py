
import numpy as np

def diamond(n):
    a, b = np.eye(n, dtype=int), np.eye(n, dtype=int)[:,::-1]
    print(a)
    print()
    print(b)

    right, left = np.concatenate((a,b)), np.concatenate((b,a))

    diamond = np.hstack((left, right[:, 1:]))
    c, d = np.hstack((b,a[:,1:])), np.hstack((a,b[:,1:]))

    return np.vstack((c, d[1:,:]))
    
def main():
    pass
    print(diamond(3))
    print(diamond(1))

if __name__ == "__main__":
    main()
