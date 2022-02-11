import math

def main():
    # enter you solution here
    
    while(True):
        shape = input('Choose a shape (triangle, rectangle, circle): ')

        if shape == '':
            break

        if shape == 'triangle':
            base = input('Give base of the triangle: ')
            height = input('Give height of the triangle: ')
            print(f'The area is {float(base)*float(height)/2}')
        
        elif shape == 'rectangle':
            width = input('Give width of the rectangle: ')
            height = input('Give height of the rectangle: ')
            print(f'The area is {float(width)*float(height)}')
        
        elif shape == 'circle':
            radius = input('Give radius of the circle: ')
            print(f'The area is {math.pi*(float(radius)**2)}')
        
        else:
            print('Unknown shape!')


if __name__ == "__main__":
    main()
