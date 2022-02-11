import re

def file_listing(filename="src/listing.txt"):
    result_list = []

    with open(filename, 'r') as f:

        for line in f:
            print('line:', line)
            iter = re.findall(r'all\s*(\d*)\s*(.{3,3})\s*(\d*)\s*(\d*)[:](\d*)\s*(.*)', line)
            # 'all\s*(\d*)\s*(.{3,3})\s*(\d*)\s*(\d*)[:](\d*)\s*(.*)'

            for (size, month, day, hour, minute, filename) in iter:
                #print(size, month, day, hour, minute, filename)
                result_list.append((int(size), month, int(day), int(hour), int(minute), filename))
            
            

    print(result_list)
    return result_list

def main():
    pass
    file_listing()

if __name__ == "__main__":
    main()
