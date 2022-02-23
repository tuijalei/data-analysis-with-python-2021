import pandas as pd

# gets a Series as a parameter
# returns a new series, whose indices and values have swapped roles
def inverse_series(s):
    return pd.Series(s.index, index=s.values)

def main():
    s = pd.Series([1,2,3], index=list('abc'))
    s_inverse = inverse_series(s)
    print(s_inverse)
    print(s_inverse[2])

if __name__ == "__main__":
    main()
