import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    '''
    gets one dimensional arrays x and y as parameters
    returns the tuple (slope, intercept) of the fitted line
    '''
    lr = LinearRegression().fit(x[:, np.newaxis],y)
    return lr.coef_[0], lr.intercept_
    
def main():
    x = np.linspace(0, 15, 10)
    y = x*2 + 1 + 1*np.random.randn(10)
    slope, intercept = fit_line(x, y)
    print(f'Slope: {slope}\nIntercept: {intercept}')
    abline_values = [slope * i + intercept for i in x]
    plt.plot(x, y, 'o')
    plt.plot(x, abline_values)
    plt.show()
    
if __name__ == "__main__":
    main()
