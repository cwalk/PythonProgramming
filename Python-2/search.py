'''
Clayton Walker
12/2/11
COP-3223H
search - program 6
A program that generates a random point in a x-y grid
user guesses what the coordinates are
'''

import random

def guess():

#Asks user to guess a x and y value for the game
    x, y = input('Enter your guess for x and y.\n').split(' ')
    x = int(x)
    y = int(y)
    return x, y

def is_correct(rand_x, rand_y, x, y, num_guesses):

#takes in the randomly generated x and y, the x and y guesses, and the counter "num_guesses"

    #Correct guess case
    if x == rand_x and y == rand_y:
        print('You got the secret location (', x ,',', y,') in ', num_guesses, ' guesses!')

    #North case
    elif x == rand_x and y < rand_y:
        print('This is not correct. You need to move N. ')

    #South case
    elif x == rand_x and y > rand_y:
        print('This is not correct. You need to move S. ')

    #East case
    elif x < rand_x and y == rand_y:
        print('This is not correct. You need to move E. ')

    #West case
    elif x > rand_x and y == rand_y:
        print('This is not correct. You need to move W. ')

    #NorthEast case
    elif x < rand_x and y < rand_y:
        print('This is not correct. You need to move NE. ')

    #NorthWest case
    elif x > rand_x and y < rand_y:
        print('This is not correct. You need to move NW. ')

    #SouthEast case
    elif x < rand_x and y > rand_y:
        print('This is not correct. You need to move SE. ')

    #SouthWest case
    elif x > rand_x and y > rand_y:
        print('This is not correct. You need to move SW. ')


def main():

#randomly generates an x and y
    rand_x = random.randint(0,9)
    rand_y = random.randint(0,9)

#declaring num_guesses and x and y variables
    num_guesses = 0
    x = -1
    y = -1

   #goes through loop to check guesses against generated ones 
    while x != rand_x:
        while y != rand_y:
        
            x, y = guess()

            num_guesses += 1
        
            is_correct(rand_x, rand_y, x, y, num_guesses)

main()
