import random
import numpy as np
word_list = np.loadtxt("/home/aishu/wordlist.txt", dtype = str)

def initial_values():
    word = random.choice(word_list)
    display = "-" * len(word)
    no_of_chances = 5
    used = []
    return word, display, no_of_chances, used


def hangman(word, display, no_of_chances, used):    
    get = raw_input("Enter a letter: ")
    
    if get in used:
        print "Warning: already used choose different letter"
        hangman(word, display, no_of_chances, used)
    
    elif (get.isalpha() == False) or (len(get) > 1):
        print "Invalid input, enter an alphabet"
        hangman(word, display, no_of_chances, used)
    
    elif get in list(word):
        used.append(get)
        indices = [i for i, x in enumerate(word) if x == get]
        for j in indices:
            display = display[0: j] + get + display[j + 1: ]
        print display
        if word == display:
            print "You won!"
            repeat = raw_input("Do you want to play again? (Enter yes or no): ")
            if repeat == "yes":
                word, display, no_of_chances, used = initial_values()
                print display
                hangman(word, display, no_of_chances, used)
            return None
        else:
            hangman(word, display, no_of_chances, used)
   
    else:
        used.append(get)
        no_of_chances = no_of_chances - 1
        if no_of_chances <= 0:
            print "You lost, the word is " + word 
            repeat = raw_input("Do you want to play again? (Enter yes or no): ")
            if repeat == "yes":
                word, display, no_of_chances, used = initial_values()
                print display
                hangman(word, display, no_of_chances,used)
            return None
        else:
            print "Wrong guess, You have " + str(no_of_chances) + " chances left"
            hangman(word, display, no_of_chances, used)
        



word, display, no_of_chances, used = initial_values()
print display
hangman(word, display, no_of_chances, used)

