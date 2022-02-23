import pandas as pd

# reads input lines from the user and return a Series
def read_series():
    idx = []
    values = []
    while True:
        text_input = input("Index and value: ")
        if not text_input:
            break
        try:
            indx, value = text_input.split()
            idx.append(indx)
            values.append(value)
        except ValueError:
            print('The input is not valid!')

    return pd.Series(values, index=idx)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
