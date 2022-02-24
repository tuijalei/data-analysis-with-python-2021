import pandas as pd

# reads in the weather DataFrame from the src
# returns the maximum amoung of snow in the year 2017
def snow_depth():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    snow = df['Snow depth (cm)']
    max_snow = snow.max()
    return max_snow

def main():
    max_snow = snow_depth()
    print(f'Max snow depth: {max_snow}')

if __name__ == "__main__":
    main()
