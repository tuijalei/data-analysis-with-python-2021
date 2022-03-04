import pandas as pd

def suicide_fractions():
    '''
     loads the data set and returns a Series that has the country as the (row) index 
     and as the column the mean fraction of suicides per population in that country.
    '''
    fractions = pd.read_csv('src/who_suicide_statistics.csv')
    fractions['fraction'] = fractions['suicides_no'] / fractions['population']
    fractions = fractions.groupby('country').mean()

    return fractions['fraction']

def main():
    df = suicide_fractions()
    print(df.shape)
    print(df.head())

if __name__ == "__main__":
    main()
