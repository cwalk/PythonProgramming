def sumPow(n, x):

#declaring sum variable
    sum = 0

#Setting up loop to go through summation n times
    for i in range(1, n + 1):
        sum += i**x

    return sum
         
def main():

#ask the user for input of n
    n = int(input('Enter n '))

#calling the function sumPow for each test case while printing the answer
    print('sum of the squares from 1 to n is', sumPow(n, 2))

    print('sum of the squares from 1 to n is', sumPow(n, 3))

    print('sum of the squares from 1 to n is', sumPow(n, .5))

main()
