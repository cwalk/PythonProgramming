def main():

#declaring variables
    room_length = int(input('What is the length of the room (in feet)? '))

    room_width = int(input('What is the width of the room (in feet)? '))

    table_length = int(input('What is the length of the table (in feet)? '))

    table_width = int(input('What is the width of the table (in feet)? '))

    table_space = int(input('How much space is required between tables (in feet?) '))

    seats_per_table = int(input('How many people does each table set? '))


#calculate the number of rows and columns possible and then the number of guests
    num_rows = int((room_length - table_space)/(table_length + table_space))

    num_cols = int((room_width - table_space)/(table_width + table_space))

    guests = int(num_rows*num_cols*seats_per_table)


#print answer
    print('This arrangement seats', guests, 'people.')

main()
