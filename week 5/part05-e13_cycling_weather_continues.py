import pandas as pd
from sklearn.linear_model import LinearRegression

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
    result = result[result['Year'] == 2017]
    result = result.groupby(['Day', 'Month', 'Year']).sum().reset_index()
    result.reset_index()

    return result

def cycling_weather():
    '''
    Merge the processed cycling data set (from the previous exercise) 
    and weather data set along the columns year, month, and day. 
    Drop useless columns 'm', 'd', 'Time', and 'Time zone'
    '''
    data1 = pd.read_csv('src/kumpula-weather-2017.csv')
    data2 = split_date_continues()

    merged_df = pd.merge(data1, data2, left_on=['Year', 'm', 'd'], right_on=['Year', 'Month', 'Day'])
    merged_df.drop(['m', 'd', 'Time', 'Time zone'], inplace = True, axis = 1)
    merged_df = merged_df.fillna(method='ffill')

    return merged_df

def cycling_weather_continues(station):
    '''
    In the linear regression use as explanatory variables the following columns 
    'Precipitation amount (mm)', 'Snow depth (cm)', and 'Air temperature (degC)'. 
    Explain the variable (measuring station), whose name is given as a parameter. 
    Fit also the intercept. 
    Return a pair, whose first element is the regression coefficients and the second element is the score. 
    '''

    df = cycling_weather()
    X = df[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = df[[station]]
    lr = LinearRegression().fit(X, y)
    return (lr.coef_[0], lr.score(X,y))
    
def main():
    station = 'Baana'
    coef, score = cycling_weather_continues(station)
    print(f'Measuring station: {station}')
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f'Score: {score:.2f}')

if __name__ == "__main__":
    main()
