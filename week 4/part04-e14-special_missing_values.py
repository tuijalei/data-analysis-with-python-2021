import pandas as pd
import numpy as np

# reads the data set of the top forty singles from the beginning of the year 1964
# returns the rows whose singles' position dropped compared to last week's position
def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df.replace({'New': None, 'Re': None}, value=None, inplace=True)
    df.dropna(axis=0, how='any', inplace=True)
    df[['Pos', 'LW']] = df[['Pos', 'LW']].astype('float')
    remain = df[df['Pos'] > df['LW']]
    return remain

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
