def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        # Começa por a
        inicio = a
    else:
        # Começa por b
        inicio = b
    for mdc in range(inicio, 0, -1):
        if (a % mdc == 0) and (b % mdc == 0):
            # É divisível pelos dois
            return mdc


def gcdRecur_(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if min(a, b) == 0:
        return max(a, b)
    else:
        return gcdRecur(b, a % b)


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return gcdRecur(b, a % b)


def fibo(n):
    ''':arg n: int
        out: int somatório de n+ (n-1) + ...
        '''
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def palindromo(texto):
    ''':arg texto: string
        out: boolean '''
    if len(texto) == 0 or len(texto) == 1:
        return True
    else:
        return texto[0] == texto[-1] and palindromo(texto[1:-1])


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    indice = len(aStr)//2
    if indice == 0:
        return False
    else:
        if aStr[indice] == char:
            return True
        else:
            if aStr[indice] > char:
                return isIn(char, aStr[:-(indice-1)])
            else:
                return isIn(char, aStr[-indice:])


print(isIn('a','bcdef'))

# print(palindromo("ablewasiereisawelba"))
# print(fibo(6))
# print('iter', gcdIter( 100, 10))
# print('rec', gcdRecur(100, 10))
# print('rec_', gcdRecur_(100, 10))
