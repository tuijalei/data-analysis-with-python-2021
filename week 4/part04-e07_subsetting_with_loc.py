import pandas as pd

# gets the subset of municipalities from Akaa to Äänekoski
# restricts it to columns: "Population", "Share of Swedish-speakers of the population, %", and "Share of foreign citizens of the population, %"
# returns this content as a DataFrame
def subsetting_with_loc():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    subset = df.loc['Akaa': 'Äänekoski', ['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return subset

def main():
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()
