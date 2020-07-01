def multi_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def mult_rec(a, b):
    if b == 1:
        return a
    else:
        return a + mult_rec(a, b-1)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def conta_p(string, count=0):
    if string.find(' ') == -1:
        return 1
    else:
        found = string.find(' ')
        string2 = string[(found+1):]
    return 1 + conta_p(string2)


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

# print(recurPower(2.5, 3))

# mdc.isIn('a','bcdef')

# L1 = [1, 28, 36]
# L2 = [2, 57, 9, -1]
# for elt in map(min, L1, L2):
#     print(elt)

# try:
#     print(1 / 0)
#     print("No error occurred!")
#
# except NameError:
#     print("A NameError occurred!")
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred!")
# except Exception:
#     print("deu merda!")
# else:
#     print('Não deu nenhum erro!')
# print("Done!")

# def string_bits(str):
#     if len(str) >0:
#         r = str[0]
#         for i in range(1, len(str)):
#             if i % 2 == 0:
#                 r += str[i]
#         return r
#     else:
#         return ''
# print(string_bits(''))

