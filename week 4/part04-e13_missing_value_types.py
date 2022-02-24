import pandas as pd
import numpy as np

# returns a dataframe
# uses the State column as the (row) index
# the two other columns should be float and object
# replaces the dashes with the appropriate missing value symbols
def missing_value_types():
    states = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    indep_year = [np.nan, 1917, 1776, 1523, np.nan, 1992]
    pres = [None, 'Niinistö', 'Trump', None, 'Steinmeier', 'Putin']
    df = pd.DataFrame({'Year of independence': indep_year, 'President':pres}, index=states) # , columns=['State', 'Year of independence', 'President'], index=states
    return df
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
