import pandas as pd

# returns the number of days when the temperature was below zero
def below_zero():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    temp = df.loc[df['Air temperature (degC)'] < 0]
    return len(temp)

def main():
    z = below_zero()
    print(f'Number of days below zero: {z}')
    
if __name__ == "__main__":
    main()
