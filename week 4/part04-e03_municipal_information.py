
import pandas as pd

def main():
    data = pd.read_csv('src/municipal.tsv', sep='\t')
    df = pd.DataFrame(data)
    print(f'Shape: {df.shape[0]}, {df.shape[1]} \nColumns:')
    for i in range(len(df.columns)):
        print(df.columns[i])


if __name__ == "__main__":
    main()
