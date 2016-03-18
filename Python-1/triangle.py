def triangle(n):
    #takes an integer n and then returns a triangle consisting of (n) many lines
    i = 1
    while (i <= n):
        print("*" * i)
        i = i + 1
    return

def main():

#ask user for n
    n = int(input('Enter n '))

#call the function to print the triangle
    triangle(n)

main()

