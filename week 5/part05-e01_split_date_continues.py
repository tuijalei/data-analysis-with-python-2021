import pandas as pd

def split_date(df):
    split_df = df['Päivämäärä'].str.split(expand=True)
    split_df.dropna(how = 'all', inplace = True)
    split_df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    split_df['Hour'] = split_df['Hour'].str.split(":", expand = True)[0]

    days = dict(zip('ma ti ke to pe la su'.split(), 'Mon Tue Wed Thu Fri Sat Sun'.split()))
    months = dict(zip('tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu'.split(), range(1,13)))

    split_df['Weekday'] = split_df['Weekday'].map(days)
    split_df['Month'] = split_df['Month'].map(months)
    #split_df.info()
    split_df = split_df.astype({'Weekday': str, 'Day': int, 'Month': int, 'Year': int, 'Hour': int})
    return split_df

def split_date_continues():
    '''
    read the bicycle data set
    clean the data set of columns/rows that contain only missing values
    drops the Päivämäärä column and replaces it with its splitted components as before
    ''' 
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    df.dropna(how = 'all', inplace = True)
    df.dropna(how = 'all', inplace = True, axis = 1)
    dates = split_date(df)
    df.drop(['Päivämäärä'], inplace = True, axis = 1)
    result = pd.concat([dates, df], axis = 1)

    return result

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
