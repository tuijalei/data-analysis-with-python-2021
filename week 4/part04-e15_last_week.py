import pandas as pd
import numpy as np

# reads the top40 data set
# reconstructs the top40 list of the previous week based on that week's list
# returns a dataframe
def last_week():
    df1 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t')
    df = df1.copy()
    df.replace(['New', 'Re'], np.nan, inplace = True)
    df = df.astype({'LW': 'float'})
    
    df['Peak Pos'].where(lambda x: (df['Peak Pos'] != df['Pos']) | (df['Peak Pos'] == df['LW']), np.nan, inplace = True)
    df['WoC'] -= 1
    df['Pos'] = df['LW']
    df = df[df['Pos'].notna()]
    df['LW'] = np.nan
    df['Pos'] = df['Pos'].astype(int)

    for i in range(1, 41):
        if i not in df['Pos'].values:
            df = df.append([{'Pos': i}])
    df.sort_values('Pos', inplace = True)
    df.reset_index(drop = True, inplace = True)

    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
