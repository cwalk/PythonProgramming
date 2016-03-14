def printline(n):

#setting up loop for printing * and stopping it at the end of the line
    i = 1
    while (i <= n):
        print('*', end = '')
        i = i + 1
    print()    

def printtri(n):

#setting up loop for printing the * triangle
    i = 1
    while (i <= n):
        printline(i)
        i = i + 1

def main():

#ask user for n
    n = int(input('Enter n '))

#call the function to print the triangle
    printtri(n)

main()

