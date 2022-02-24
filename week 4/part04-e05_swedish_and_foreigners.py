
import pandas as pd

# returns DataFrame which contains municipalities which have proportion
# of Swedish speaking people and proportion of foreigners both above 5%
# note: only column about population and the proportions of Swedish speaking people and foreigners 
def swedish_and_foreigners():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    municipalities = df['Akaa':'Äänekoski']
    swed_and_foreign = municipalities[(municipalities['Share of Swedish-speakers of the population, %'] > 5) & (municipalities['Share of foreign citizens of the population, %'] > 5)]
    swed_and_foreign = swed_and_foreign[['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return swed_and_foreign

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
