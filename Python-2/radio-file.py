'''
Clayton Walker
11/23/11
COP-3223H
radio-files - program 6
Radio Censor program re-written, to take input from a file
'''

def main():

#declaring lists
    censored_words = []
    uncensored_words = []
    replacement = []
    string = ''    

#prompt user for input file to read from
    input_filename = input('What is the input file?\n')

#prompt user for output file to write
    output_filename = input('What file do you want to store your output?\n')

#open file
    f = open(input_filename, 'r')

#reading number of pairs of censored/uncensored words 
    n = f.readline()
    n = int(n)
    
#setting up loop to go through each pair, and append them to their
#respective lists
    
    for num in range(n): 
        pair = f.readline()
        censored_words.append(pair.split(' ')[0])
        uncensored_words.append(pair.split(' ')[1].split('\n')[0])

#delcaring len, the number of lines in the message to translate.
    len = f.readline()
    len = int(len)

#setting sentence to be read in from file, sentences is all 3 sentences joined
    sentence = ''
    sentences = []
    for num in range(len): 
        sentence = f.readline()
        sentences.append(sentence)
        
#makes 'sentence' now be 'sentences' combined
    sentence = ''.join(sentences)

#close input file
    f.close()

#splitting sentences into words
    uncensored_sentence = sentence.split(' ')

#setting up for loop to check each word in the sentence entered by user
#and if a word that needs to be censored is in it, go into if statement
    for word in uncensored_sentence:
        if word in censored_words:
            index = censored_words.index(word)
            replacement.append(uncensored_words[index])

        else:
           replacement.append(word)


#print censored sentence in output file
    string = ' '.join(replacement)
    f = open(output_filename, 'w')
    f.write(string)
    f.close()

#print out sucessful message
    print('Your message has been stored! ')

main()
