import pandas as pd

def top_bands():
    '''
    Merge the DataFrames UK top40 and the bands DataFrame.
    Use the left_on and right_on parameters to merge.
    '''
    bands = pd.read_csv('src/bands.tsv', sep = '\t')
    UK_top = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t')
    bands['Band'] = bands['Band'].str.upper()
    df = pd.merge(bands, UK_top, left_on = 'Band', right_on = 'Artist')
    return df

def main():
    df = top_bands()
    print(df.shape)
    print(df.columns)
    print(df.head())

if __name__ == "__main__":
    main()
