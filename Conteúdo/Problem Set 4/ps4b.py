from ps4a import *
import time


#
#
# Computer chooses a word
#
#
from ProblemSet4 import ps4a

def compChooseWord_melhorado(hand, wordList, n, words, score, validWords):
    """
    Rotina de uma colega do curso: "bbye98"

    repetirá todas as combinações possíveis de palavras válidas usando uma árvore de decisão/recursão.
    Não é apenas muito mais rápido para n <9, mas também às vezes encontra jogadas com pontuação mais alta!
    No entanto, com mais opções, a natureza recursiva do código a seguir torna muito mais lento que
    a força bruta verificando cada entrada na lista de palavras para n ≥ 9.

    Nota: Eu adicionei um parâmetro para isValidWordignorar a verificação se a palavra está na
    lista de palavras para economizar tempo, por exemplo isValidWord(word, hand, wordList, checkWordList=True)

    """
    best = None
    bestScore = -1
    bestWords = []
    for validWord in validWords:
        curHand = updateHand(hand, validWord)
        curScore = score + getWordScore(validWord, n)
        curWords = words + [validWord]
        curValidWords = getValidWords(curHand, wordList, n)
        curWords, curScore = compChooseWord(curHand, wordList, n, curWords, curScore, curValidWords)
        if curScore > bestScore:
            best = validWord
            bestWords = curWords
            bestScore = curScore
    if best is None:
        return words, score
    return bestWords, bestScore

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

def compPlayHand_melhorado(hand, wordList, n):
    """
    Rotina de uma colega do curso: "bbye98"

    repetirá todas as combinações possíveis de palavras válidas usando uma árvore de decisão/recursão.
    Não é apenas muito mais rápido para n <9, mas também às vezes encontra jogadas com pontuação mais alta!
    No entanto, com mais opções, a natureza recursiva do código a seguir torna muito mais lento que
    a força bruta verificando cada entrada na lista de palavras para n ≥ 9.

    Nota: Eu adicionei um parâmetro para isValidWordignorar a verificação se a palavra está na
    lista de palavras para economizar tempo, por exemplo isValidWord(word, hand, wordList, checkWordList=True)

    """
    bestWords, _ = compChooseWord(hand, wordList, n, [], 0, getValidWords(hand, wordList, n))
    score = 0
    for word in bestWords:
        print('\nCurrent hand: ' + displayHand(hand) + '\nEnter a word or "." to indicate that you are finished: ' + word)
        wordScore = getWordScore(word, n)
        hand = updateHand(hand, word)
        score += wordScore
        print('"' + word + '" earned %d points. Total: %d points.\n' % (wordScore, score))
    if sum(hand.values()) > 0:
        word = '.'
        print('Current hand: ' + displayHand(hand) + '\nEnter a word or "." to indicate that you are finished: ' + word)
    print(('Goodbye! ' if word is '.' else 'Ran out of letters. ') + 'Total score: %d points.\n' % score)

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # Fazendo...
    try:
        type(hand)
    except NameError:
        hand ={}

    def pessoa_pc():
        while True:
            escolha = input('Enter u to have yourself play, c to have the computer play:')
            if escolha == 'u':
                #Humano
                ps4a.playHand(hand, wordList, HAND_SIZE)
                break
            elif escolha == 'c':
                #PC
                compPlayHand(hand, wordList, HAND_SIZE)
                break
            else:
                print('Invalid command.')


    while True:
        escolha = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if escolha == 'n': #Nova mão
            hand = ps4a.dealHand(HAND_SIZE)
            pessoa_pc()

        elif escolha == 'r': #Jogar mão anterior
            if len(hand) == 0:
                print('You have not played a hand yet. Please play a new hand first!\n')
            else:
                pessoa_pc()

        elif escolha == 'e':
            # Sai do jogo
            break
        else:
            print('Invalid command.')

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

    # print(compPlayHand(
    #     {'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1},
    #     wordList, 6))

