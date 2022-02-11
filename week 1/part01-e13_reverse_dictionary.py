
def reverse_dictionary(d):
    new_dic = {}
    for k,v in d.items():
        for x in v:
            new_dic.setdefault(x,[]).append(k)

    print(new_dic)
    return new_dic

def main():
    pass
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
