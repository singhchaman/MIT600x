# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
        else:
            continue
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    temp=list()
    ret=list()
    for i in lettersGuessed:
        if i in secretWord:
            temp.append(i)
    for i in secretWord:
        if i in temp:
             ret.append(i)
        else:
            ret.append('_ ')
    ret=''.join(ret)
    return ret



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    temp=list()
    ret=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in lettersGuessed:
        ret.remove(i)
    ret=''.join(ret)
    return ret
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ', len(secretWord), 'letters long'
    print '-----------'
    guessesLeft=8
    lettersGuessed=[]
    while 1:        
        print 'You have ', guessesLeft, ' guesses left.'
        print 'Available letters: ',
        print getAvailableLetters(lettersGuessed)
        letter=raw_input('Please guess a letter: ')
        letter=letter.lower()
        if letter in lettersGuessed:
            lettersGuessed.append(letter)
            print 'Oops! You\'ve already guessed that letter: ',
            print getGuessedWord(secretWord, lettersGuessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print 'Good guess: ',
            print getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(letter)
            print 'Oops! That letter is not in my word: ',
            print getGuessedWord(secretWord, lettersGuessed)
            guessesLeft-=1
        print '-----------'
        if getGuessedWord(secretWord, lettersGuessed)==secretWord and guessesLeft>0:
            print 'Congratulations, you won!'
            break
        elif guessesLeft==0:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'
            break






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
