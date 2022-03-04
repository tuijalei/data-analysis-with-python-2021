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


def cycling_weather():
    '''
    Merge the processed cycling data set (from the previous exercise) 
    and weather data set along the columns year, month, and day. 
    Drop useless columns 'm', 'd', 'Time', and 'Time zone'
    '''
    cycling_data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    weather_data = pd.read_csv('src/kumpula-weather-2017.csv', sep = ',')
    cycling_data = cycling_data.dropna(how = 'all', axis = 0)
    cycling_data = cycling_data.dropna(how = 'all', axis = 1)

    dates = split_date(cycling_data)

    cycling_data = cycling_data.drop(['Päivämäärä'], axis = 1)
    concat_df = pd.concat([dates, cycling_data], axis = 1)
    merged_df = pd.merge(concat_df, weather_data, left_on=['Year', 'Month', 'Day'], right_on=['Year', 'm', 'd'])
    merged_df.drop(['m', 'd', 'Time', 'Time zone'], inplace = True, axis = 1)

    return merged_df

def main():
    df = cycling_weather()
    print(df.shape)
    print(df.head())

if __name__ == "__main__":
    main()
