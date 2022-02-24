import pandas as pd
import numpy as np

# reads the table from the tsv file
# returns the cleaned version of it
# edits programmatically using the string edit methods
# columns dtypes: object, integer, float, integer, object
def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep = '\t')
    df['Start'] = df['Start'].str.split(expand = True)[:][0]
    df['Seasons'] = df['Seasons'].str.replace('two', '2', regex = False)
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')

    df['President'] = df['President'].str.replace(r'(\w+), *(\w+)', r'\2 \1').str.title()
    df['Vice-president'] = df['Vice-president'].str.replace(r'(\w+), *(\w+)', r'\2 \1').str.title()
    
    df = df.astype({'President': object,'Start': int, 'Last': float, 'Seasons': int, 'Vice-president': object})
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
