

def transform(s1, s2):
    if not s1 and not s2:
        return []

    all = list(zip(s1.split(' '), s2.split(' ')))
    result = list(map(lambda x: int(x[0])*int(x[1]), all))
    
    return result

def main():
    pass
    print(transform("1 5 3", "2 6 -1"))
    print(transform('', ''))

if __name__ == "__main__":
    main()
