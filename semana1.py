"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""
s = 'azcbobobegghakl'
vogal = ['a','e','i','o','u']
vogais = 0

for indice in s:
    if indice in vogal:
        vogais += 1
# print('Number of vowels:', vogais)

"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
s = 'azcbobobegghakl'

# Solução 1: Sem utilização de métodos string
procura = 'bob'
localizadas = 0

for conjunto in range(len(s)-len(procura)+1):
    # print(conjunto, s[conjunto:conjunto+3])
    if procura == s[conjunto:conjunto+3]:
        localizadas += 1
# print('Number of times {} occurs is:' .format(procura), localizadas)

# Solução 2: Com utilização de métodos de string
procura = 'bob'
localizadas = 0
indice = s.find(procura)

while indice > 0:
    indice += 1
    localizadas += 1
    indice = s.find(procura, indice)

# print('Number of times {} occurs is:' .format(procura), localizadas)

""" 
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur 
in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print:
Longest substring in alphabetical order is: abc

Note: This problem may be challenging. 
We encourage you to work smart. 
If you've spent more than a few hours on this problem, 
we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.
"""
s = 'zyxwvutsrqponmlkjihgfedcba'


seq_atual = s[0]
acumula = seq_atual

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        seq_atual += s[i+1]
        if len(seq_atual) > len(acumula):
            acumula = seq_atual
    else:
        seq_atual = s[i+1]

print('Longest substring in alphabetical order is:', acumula)