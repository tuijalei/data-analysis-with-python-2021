import sys

# count the number of lines, words, and characters
def file_count(filename):
    words = []
    line_counter = 0
    char_counter = 0
    with open(filename, 'r') as f:
        for line in f:
            line_counter += 1
            char_counter += len(line)
            line_words = line.split()
            
            for word in line_words:
                words.append(word) #.strip("""!"#$%&'()*,-./:;?@[]_""")

    #print(line_counter)
    #print(char_counter)
    #print(len(words))

    return (line_counter, len(words), char_counter)

def main():
    pass
    for file in sys.argv[1:]:
        outputs = file_count(file)
        print(f'{outputs[0]}\t{outputs[1]}\t{outputs[2]}\t{file}')

if __name__ == "__main__":
    main()
