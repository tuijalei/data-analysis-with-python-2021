import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    '''
    reads this file and learns and
    returns the regression coefficients for the five features
    '''
    data = pd.read_csv('src/mystery_data.tsv', sep = '\t')
    lr = LinearRegression(fit_intercept = False).fit(data.iloc[:, 0:5], data.iloc[:, 5])
    return lr.coef_

def main():
    coefficients = mystery_data()
    for i, coef in enumerate(coefficients):
        print(f'Coefficient of X{i+1} is {coef}')
    
if __name__ == "__main__":
    main()
