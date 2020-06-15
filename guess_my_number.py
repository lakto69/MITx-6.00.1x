print('Please think of a number between 0 and 100!')
max = 100
min = 0
resp = ''
while resp != 'c':
    palpite = int((max+min)/2)
    print('Is your secret number', palpite, '?')
    resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while resp not in ['h','l','c']:
        print('Sorry, I did not understand your input.')
        print('Is your secret number', palpite, '?')
        resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if resp == 'c':  # Acertou!
        print('Game over. Your secret number was: ', palpite)
    elif resp == 'l':  # Valor baixo, tentar na parte superior
        min = palpite
    else:  # Valor alto, Tentar na parte inferior
        max = palpite