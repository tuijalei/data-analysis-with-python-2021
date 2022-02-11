import re

def integers_in_brackets(s):
    '''
    \[ - a [ char
    \s* - 0+ whitespaces
    (?:\+(?=\d))? - an optional + that must be followed with a digit
    (-?\d+) - Group 1: an optional - and then 1+ digits
    \s* - 0+ whitespaces
    ] - a ] char.

    '''
    return list(map(int, re.findall(r"\[\s*(?:\+(?=\d))?(-?\d+)\s*]",s)))

def main():
    pass
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
