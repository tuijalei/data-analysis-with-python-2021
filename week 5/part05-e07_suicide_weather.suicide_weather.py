from audioop import avg
import pandas as pd

def suicide_fractions():
    fractions = pd.read_csv('src/who_suicide_statistics.csv')
    fractions['fraction'] = fractions['suicides_no'] / fractions['population']
    fractions = fractions.groupby('country').mean()
    return fractions['fraction']

def suicide_weather():
    '''
    Returns a tuple (suicide_rows, temperature_rows, common_rows, spearman_correlation)
    '''
    avg_temps = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col = 0, header = 0)[0]
    avg_temps['Average yearly temperature (1961–1990, degrees Celsius)'] = avg_temps['Average yearly temperature (1961–1990, degrees Celsius)'].str.replace('\u2212', '-')
    avg_temps['Average yearly temperature (1961–1990, degrees Celsius)'] = avg_temps['Average yearly temperature (1961–1990, degrees Celsius)'].astype('float')
    avg_temps.sort_index(inplace = True)

    fractions = suicide_fractions()
    fractions.sort_index(inplace = True)

    common_df = avg_temps.merge(right = fractions, left_index = True, right_index = True)
    spear_corr = common_df['fraction'].corr(common_df['Average yearly temperature (1961–1990, degrees Celsius)'], method = 'spearman')

    return (len(fractions), len(avg_temps), len(common_df), spear_corr)

def main():
    s_row, temp_row, com_row, spearman = suicide_weather()
    print(f'Suicide DataFrame has {s_row} rows')
    print(f'Temperature DataFrame has {temp_row} rows')
    print(f'Common DataFrame has {com_row} rows')
    print(f'Spearman correlation: {spearman}')

if __name__ == "__main__":
    main()
