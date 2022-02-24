import pandas as pd
import numpy as np

# reads the bicycle data set and clean it
# splits the Päivämäärä column into a DataFrame with five columns with column names Weekday, Day, Month, Year, and Hour
# returns a DataFrame with five columns
# ma -> Mon
# ti -> Tue
# ke -> Wed
# to -> Thu
# pe -> Fri
# la -> Sat
# su -> Sun
# tammi -> 1, helmi -> 2, maalis -> 3 etc
def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    split_df = df['Päivämäärä'].str.split(expand=True)
    split_df.dropna(inplace = True)
    split_df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    split_df['Hour'] = split_df['Hour'].str.split(":", expand = True)[0]

    days = dict(zip('ma ti ke to pe la su'.split(), 'Mon Tue Wed Thu Fri Sat Sun'.split()))
    months = dict(zip('tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu'.split(), range(1,13)))

    split_df['Weekday'] = split_df['Weekday'].map(days)
    split_df['Month'] = split_df['Month'].map(months)
    #split_df.info()
    split_df = split_df.astype({'Weekday': str, 'Day': int, 'Month': int, 'Year': int, 'Hour': int})
    return split_df

def main():
    print(split_date())
       
if __name__ == "__main__":
    main()
