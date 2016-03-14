import math

def main():

#asking user input on a b and c
    a = int(input('Enter a '))

    b = int(input('Enter b '))

    c = int(input('Enter c '))

#calcultaing the discrinant (under the square root)
    discriminant = math.sqrt(b**2 - 4*a*c)


#finding the positive and negative roots
    root_positive = (-b + (discriminant))/(2*a)

    root_negative = (-b - (discriminant))/(2*a)
    

#printing out the answer
    print('Your roots are', root_positive, 'and', root_negative,'.')

main()
