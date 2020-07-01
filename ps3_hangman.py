# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    secretWord: string, a palavra que o usuário está adivinhando
    lettersGuessed: list, que letras foram adivinhadas até agora
    returns: boolean, True se todas as letras de secretWord estiverem em lettersGuessed;
        Falso caso contrário
    '''
    # FILL IN YOUR CODE HERE...
    for letra in secretWord:
       if letra not in lettersGuessed:
           return False

    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, a palavra que o usuário está adivinhando
    lettersGuessed: list, que cartas foram adivinhadas até agora
    returns: string, composto por letras e sublinhados que representam
        quais letras em segredoWord foram adivinhadas até agora.
    '''
    # FILL IN YOUR CODE HERE...
    palavra = ''
    for letra in secretWord:
       if letra not in lettersGuessed:
            palavra += ' _'
            # print('não', letra, palavra)
       else:
            palavra += ' ' + letra
            # print('sim', letra, palavra)
    # print('dentro', palavra)
    return palavra

# print(getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's'] #['e', 'a', 'k', 'b', 'r', 'l']
# print(getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, que letras foram adivinhadas até agora
    returns: string, composto por letras que representam quais letras
        que ainda não foram adivinhadas.
    '''
    # FILL IN YOUR CODE HERE...
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    sobram = ''
    for letra in alfabeto:
        if letra not in lettersGuessed:
            sobram += letra
    return sobram

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

def hangman(secretWord):
    '''
    secretWord: string, a palavra secreta para adivinhar.

    Inicia um jogo interativo de forca.

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
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.' .format(len(secretWord)))

    # RETIRAR ESSA LINHA QUANDO PUBLICAR!!!!!:
    # print('I am thinking of a word that is {} letters long. ({})'.format(len(secretWord), secretWord))

    mistakesMade = 8
    lettersGuessed = []

    while mistakesMade > 0:
        print('-------------')
        print('You have {} guesses left.'.format(mistakesMade))
        print('Available letters:', getAvailableLetters(lettersGuessed))

        pergunta = input('Please guess a letter:').lower()
        if pergunta in lettersGuessed:
            print("Oops! You've already guessed that letter:", certas)
        else:
            lettersGuessed.append(pergunta)
            certas = getGuessedWord(secretWord, lettersGuessed)

            if lettersGuessed[len(lettersGuessed)-1] in secretWord:
                print('Good guess:', certas)
            else:
                mistakesMade -= 1
                print("Oops! That letter is not in my word:", certas)
                if mistakesMade == 0:
                    print('-------------')
                    print('Sorry, you ran out of guesses. The word was else.')

            if isWordGuessed(secretWord, lettersGuessed): # Acertou a palavra inteira!!
                print('-------------')
                print('Congratulations, you won!')
                break






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
