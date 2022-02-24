from numpy import average
import pandas as pd

# reads the weather data set
# returns the average temperature in July (7th month)
def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    july = df.loc[df['m'] == 7] # July (7th month)
    temp = july['Air temperature (degC)']
    return temp.mean()

def main():
    avg_temp = average_temperature()
    print(f'Average temperature in July: {avg_temp}')

if __name__ == "__main__":
    main()
