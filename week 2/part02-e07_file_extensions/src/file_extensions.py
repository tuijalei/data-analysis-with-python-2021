import re
import os

def file_extensions(filename):
    no_ext = []
    ext_files = {}

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('.')
            value = line.strip()

            if len(parts) == 1:
                no_ext += parts
            
            else:
                key = re.findall(r'.*\.(\w*)', line) # returns list
                #print(key)
                key = ''.join(key) # returns string

                if key not in ext_files:
                    ext_files[key] = [value]
                else:
                    ext_files[key] += [value]
    
    #print(no_ext)
    #print(ext_files)
    return (no_ext, ext_files)

def main():
    pass
    no_ext, extension = file_extensions('src/filenames.txt')
    
    print(f'{len(no_ext)} files with no extension')
    for key in sorted(extension.keys()):
        print(key, len(extension[key]))

if __name__ == "__main__":
    main()
