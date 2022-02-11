
def word_frequencies(filename='src/alice.txt'):
    word_list = []

    with open(filename) as f:
        for line in f:
            words = line.split()
            
            for word in words:
                word_list.append(word.strip("""!"#$%&'()*,-./:;?@[]_"""))
    
    #print(word_list)
    word_frec = []
    for word in word_list:
        word_frec.append(word_list.count(word))
    
    #print(word_frec)

    result_dict = dict(zip(word_list, word_frec))
    #print(result_dict)
    return result_dict

def main():
    pass
    word_frequencies()

if __name__ == "__main__":
    main()
