
def sum_equation(L):
    if not L:
        return '0 = 0'

    num_to_str = list(map(str, L))
    result_str = ' + '.join(num_to_str)
    return f'{result_str} = {sum(L)}'

def main():
    pass
    print(sum_equation([1,5,7]))
    print(sum_equation([]))

if __name__ == "__main__":
    main()
