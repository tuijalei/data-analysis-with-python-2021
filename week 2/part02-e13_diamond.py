
import numpy as np

def diamond(n):
    a, b = np.eye(n, dtype=int), np.eye(n, dtype=int)[:,::-1]
    top = np.concatenate((b,a[:, 1:]), axis=1)
    bottom = np.concatenate((a,b[:, 1:]), axis=1)
    diamond = np.concatenate((top, bottom[1:]), axis=0)
    return diamond
    
def main():
    pass
    print(diamond(3))
    print(diamond(1))

if __name__ == "__main__":
    main()
