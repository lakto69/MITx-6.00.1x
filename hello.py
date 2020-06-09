def right_justify(texto=''):
    ''' Recebe um string e imprime na tela no extremo direito
    dela. Tela com 70 posições
    '''
    print(70*'-')
    if len(texto) > 70:
        print('Texto muito longo! Tente com um texto menor do 70 posições')
    elif len(texto) == 70:
        print(texto)
    else:
        vezes = 70 - len(texto)
        print(vezes*" " + texto)

right_justify('monty')