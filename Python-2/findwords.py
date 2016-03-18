'''
Clayton Walker
11/20/11
COP-3223H
findwords - program 6
A python program that asks the user to enter a sentence
and prints out each separate word in that sentence.
'''

def main():

#ask user for sentence
    original_sentence = raw_input('What is your sentence?\n')

#Set new variable fixed_sentence
    fixed_sentence = ""

#Get rid of all punctuation including ,.?!;:' and "
    for i in original_sentence:
        if i in ',.?!;:\'"':
            i = ""
        fixed_sentence += i

#print the new sentence
    print('The words in your sentence are')
    print(fixed_sentence)

main()
