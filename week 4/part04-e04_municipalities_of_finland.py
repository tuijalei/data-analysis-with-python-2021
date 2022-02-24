
import pandas as pd

# returns a DataFrame containing only rows about municipalities
# rows from Akaa to Äänekoski are municipalities of Finland in alphabetical order
def municipalities_of_finland():
    data = pd.read_csv('src/municipal.tsv', sep='\t', index_col='Region 2018')
    df = pd.DataFrame(data['Akaa': 'Äänekoski'])
    return df
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
