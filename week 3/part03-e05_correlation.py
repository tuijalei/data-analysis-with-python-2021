
import scipy.stats as stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

# Loads the data and returns the correlation between sepal_length and petal length 
# Indeces are as
# 0: sepal length (cm)
# 1: sepal width (cm)   
# 2: petal length (cm)   
# 3: petal width (cm)  
def lengths():
    all_data = load()
    sepal_lengths = all_data[:, 0]
    petal_lengths = all_data[:, 2]

    # [0] since the first element is the correlation
    return stats.pearsonr(sepal_lengths, petal_lengths)[0]

# Compute the Pearson correlation between all the variables
# returns an array of shape (4,4) containing the correlations
# Indeces are as
# 0: sepal length (cm)
# 1: sepal width (cm)   
# 2: petal length (cm)   
# 3: petal width (cm)  
def correlations():
    all_data = load()
    sepal_lengths = all_data[:, 0]
    sepal_widths = all_data[:, 1]
    petal_lengths = all_data[:, 2]
    petal_widths = all_data[:, 3]
    
    return np.corrcoef((sepal_lengths, sepal_widths, petal_lengths, petal_widths))

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
