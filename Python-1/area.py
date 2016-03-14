def main():

#asking user for input on length and width variables
    length = int(input('What is the length of the rectangle? '))

    width = int(input('What is the width of the rectangle? '))


#setting up equations for perimieter and area
    perimeter = 2*length + 2*width

    area = length*width


#printing out input
    print('The perimeter of the rectangle is', perimeter, 'units.')

    print('The area of the rectangle is ', area, 'square units.')

main()
