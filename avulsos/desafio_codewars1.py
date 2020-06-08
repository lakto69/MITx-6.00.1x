import re
def iq_test(numbers):
    #padrão de procura
    p = re.compile('[0-9]\s|[0-9]*')
    a=[]
    for numeros in p.findall(numbers):
        if len(numeros) > 0:
            if int(numeros)%2 == 0:
                a.append('p')
            else:
                a.append('i')
    if a.count('p') > 1: #Tem mais pares
        return a.index('i') + 1
    else:#Tem mais ímpares
        return a.index('p') + 1

v="2 4 7 8 10"
# v='10 58 4 23'

r=iq_test(v)
print(v, '=', r)