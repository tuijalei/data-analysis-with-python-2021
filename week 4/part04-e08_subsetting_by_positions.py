import pandas as pd

# returns the top 10 entries and only the columns Title and Artist
def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t', index_col=0)
    subset = df.iloc[0:10, [1, 2]] # only 10 first rows, columns 1 and 2
    return pd.DataFrame(subset)

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()
