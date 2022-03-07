import pandas as pd
import matplotlib.pyplot as plt

def split_date(df):
    '''
    reads the bicycle data set and clean it
    splits the Päivämäärä column into a DataFrame with five columns with column names Weekday, Day, Month, Year, and Hour
    returns a DataFrame with five columns
    '''
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

def bicycle_timeseries():
    '''
    reads the data set
    cleans it
    turns its Päivämäärä column into (row) DatetimeIndex (that is, to row names) of that DataFrame
    returns the new DataFrame
    '''
    
    df = split_date_continues()
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])
    df.drop(columns = ['Year', 'Month', 'Day', 'Hour'], inplace = True)
    df.set_index('Date', inplace = True)
    return df


def commute():
    '''
    Restrict to August 2017, group by the weekday, aggregate by summing. 
    Set the Weekday column to numbers from one to seven. 
    Then set the column Weekday as the (row) index. 
    Return the resulting DataFrame from the function.
    '''

    df = bicycle_timeseries()
    df = df['2017-08-01':'2017-08-31']
    days = dict(zip("Mon Tue Wed Thu Fri Sat Sun".split(), range(1,8)))
    df["Weekday"] = df["Weekday"].map(days)
    df = df.groupby('Weekday').sum()

    return df
    
def main():
    df = commute()
    print(df.shape)
    print(df.head())
    plt.plot(df)
    plt.show()

if __name__ == "__main__":
    main()
