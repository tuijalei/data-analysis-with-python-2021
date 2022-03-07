import pandas as pd
from sklearn.linear_model import LinearRegression

def coefficient_of_determination():
    data = pd.read_csv('src/mystery_data.tsv', sep = '\t')
    X = data.iloc[:, 0:5]
    y = data.iloc[:, 5]
    lr = LinearRegression().fit(X, y)
    deters = [lr.score(X, y)]

    for col in X:
        fitted = data[col].values.reshape(-1, 1)
        lr.fit(fitted, y)
        deters.append(lr.score(fitted, y))

    return deters
    
def main():
    det_coefs = coefficient_of_determination()
    print(f'R2-score with feature(s) X: {det_coefs[0]}')
    for i, coef in enumerate(det_coefs):
        print(f'R2-score with feature(s) X{i+1}: {coef}')

if __name__ == "__main__":
    main()
