import pandas as pd

# takes a Series and a positive integer k as parameters
# returns a DataFrame:
# > first column should be the input Series
# > the second column should contain the Series raised to power of two
# > he third column should contain the Series raised to the power of three
# > so on until (and including) power of k
def powers_of_series(s, k):
    df = pd.DataFrame([])
    for i in range(1, k + 1):
        df.insert(i-1, i, s**i)
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list('abcd'))
    print(powers_of_series(s, 5))
    
if __name__ == "__main__":
    main()
