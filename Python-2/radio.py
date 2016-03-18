'''
Clayton Walker
11/20/11
COP-3223H
radio - program 6
A program that reads in a message and changes
each censored word to its uncensored equivalent.
'''

def main():

#ask user for number of censored words, and each pair of censored words
    n = int(input('How many censored words are there?\n'))

#Set lists for censored words, uncensored words, and its replacement
    censored_words = []
    uncensored_words = []
    replacement = []
    string = ''

#setting up loop to go through each pair, and append them to their
#respective lists
    
    for num in range(n):
                pair = raw_input('Please enter censored/uncensored pair #%d:\n' %(num + 1))
                censored_words.append(pair.split(' ')[0])
                uncensored_words.append(pair.split(' ')[1])
       
#Prompt user for their sentence and break it apart into words
    sentence = raw_input('Please enter a sentence with lowercase letters only:\n')
    uncensored_sentence = sentence.split(' ')

#setting up for loop to check each word in the sentence entered by user
#and if a word that needs to be censored is in it, go into if statement
    for word in uncensored_sentence:
        if word in censored_words:
            index = censored_words.index(word)
            replacement.append(uncensored_words[index])

        else:
           replacement.append(word)


#print censored sentence and put it back together
    print('The censored sentence is as follows:')
    string = ' '.join(replacement)
    print(string)

main()
