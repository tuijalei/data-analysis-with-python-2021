import pandas as pd

def best_record_company():
    '''
    Define "goodness" of a record company (Publisher) based on the sum of the weeks on chart (WoC) of its singles.
    Return a DataFrame of the singles by the best record company.
    '''
    UK_top = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep= '\t')
    top_records = UK_top.groupby('Publisher')
    top_pub = top_records.sum()['WoC'].idxmax()
    singles_df = UK_top[UK_top['Publisher'] == top_pub]
    return singles_df

def main():
    df = best_record_company()
    print(df.shape)
    print(df)

if __name__ == "__main__":
    main()
