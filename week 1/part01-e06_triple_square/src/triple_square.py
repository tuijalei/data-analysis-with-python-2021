
def main():
    pass

    for i in range(1, 11):
        tr = triple(i)
        sq = square(i)

        if sq > tr:
            break

        print(f'triple({i})=={tr} square({i})=={sq}')
        

def triple(a):
    return a*3

def square(a):
    return a**2

if __name__ == "__main__":
    main()
