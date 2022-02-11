from cmath import exp


def extract_numbers(s):
    result = []
    parts = s.split()

    for part in parts:
        try:
            x = int(part)
            result.append(x)
            continue
        except Exception:
            print('Couldn`t convert to int, wrong value')
        
        try:
            x = float(part)
            result.append(x)
            continue
        except Exception:
            print('Couldn`t convert to float, wrong value')
        
    print(result)
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
