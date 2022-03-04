import pandas as pd
import matplotlib.pyplot as plt

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

def cyclists_per_day():
    '''
    Read, clean and parse the bicycle data set as before. 
    Group the rows by year, month, and day. 
    Get the sum for each group.
    '''
    cycling_data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    cycling_data = cycling_data.dropna(how = 'all', axis = 0).dropna(how = 'all', axis = 1)
    dates = split_date(cycling_data)
    cycling_data.drop(['Päivämäärä'], inplace = True, axis = 1)
    
    concat_df = pd.concat([dates, cycling_data], axis = 1)
    concat_df.drop(['Hour', 'Weekday'], inplace = True, axis = 1)
    grouped_df = concat_df.groupby(['Year', 'Month', 'Day']).sum()
    return grouped_df
    
def main():
    df = cyclists_per_day()
    plt.plot(df.loc[(2017, 8)]) # restrict this data to August of year 2017, and plot this data. 
    plt.show()

if __name__ == "__main__":
    main()
