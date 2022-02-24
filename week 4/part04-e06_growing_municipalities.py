import pandas as pd

# gets subset of municipalities (a DataFrame) as a parameter
# returns the proportion of municipalities with increasing population in that subset
def growing_municipalities(df):
    col = df["Population change from the previous year, %"]
    count_mun = len(col)
    result_df = df[df['Population change from the previous year, %'] > 0]
    count_inc = len(result_df)
    return count_inc/count_mun

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    df = df['Akaa':'Äänekoski']
    increasing_pop = growing_municipalities(df)
    print(f'Proportion of growing municipalities: {increasing_pop:.1f}%') # 1 decimal precision

if __name__ == "__main__":
    main()
