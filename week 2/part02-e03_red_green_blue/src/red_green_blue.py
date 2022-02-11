import re

def red_green_blue(filename="src/rgb.txt"):
    result_list = []

    with open(filename, 'r') as f:
        # first line out
        rows = f.readlines()[1:]

        for line in rows:
           # row = re.findall('[0-9]{0,3}\w+', line) 
            row = re.findall(r'(\d+)[\s]*(\d+)[\s]*(\d+)[\s]*(.*)', line)
            #print(row.pop())
            new_row = '\t'.join(row.pop())
            print(type(new_row), new_row, len(new_row))
        
            result_list.append(new_row)

    print(result_list)
    return result_list


def main():
    pass
    red_green_blue()

if __name__ == "__main__":
    main()
