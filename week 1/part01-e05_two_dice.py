
def main():
    pass

    for i in range(1, 7):
        for j in range(1, 7):
            
            if i + j != 5:
                continue
            
            print(f'({i},{j})')
    

if __name__ == "__main__":
    main()
