import pandas as pd

# return cleaned dataset without missing values
def cyclists():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    df.dropna(how = 'all', inplace = True)
    df.dropna(axis = 1, how = 'all', inplace = True)
    return df


def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
