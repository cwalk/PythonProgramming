'''
Clayton Walker
11/25/11
COP-3223H
invite - program 6
Re-write invite in python
'''

import math

def main():

#set constants for size of packages
    SMALL_SIZE = 50
    LARGE_SIZE = 200

#prompt user for input on cost of packages and # of invites being sent
    cost_small = float(input('What is the cost of a small package (in dollars)?\n'))
    cost_large = float(input('What is the cost of a large package (in dollars)?\n'))
    number_invites = int(input('How many invitations are you sending out?\n'))

#Declaring each number of packages at start
    num_small = 0
    num_large = 0

#large package cheaper case
    if cost_large <= cost_small:
        num_large = math.ceil(float(number_invites)/LARGE_SIZE)

#small packages case for cheaper
    elif cost_small/SMALL_SIZE <= cost_large/LARGE_SIZE:
        num_small = math.ceil(float(number_invites)/SMALL_SIZE)

#real life case in which larger packages are better deal
    else:
        #Buy large in this case
        num_large = number_invites//LARGE_SIZE;

        rest = int(number_invites%LARGE_SIZE)
        
        #Find number of small packages
        temp_small = int(math.ceil(float(rest)/SMALL_SIZE))

        #If the small packages are best deal
        if temp_small*cost_small < cost_large:
            num_small = temp_small

        #If it can fit in one large package as cheapest way
        else:
            num_large += 1

    # Calculate cost
    cost = float(num_small*cost_small + num_large*cost_large)
    
#print out answer
    print('You should order ', num_small, 'small package(s).')
    print('You should order ', num_large, 'large package(s).')
    print('Your cost for invitations will be $%.2f.'% round(cost, 2))

main()
