# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:53:38 2020

@author: leite.aml
"""
#   '0123456789012345678901234567890
s = 'zydjrwcyjslqgypl'

i = 0
trechoG = s[0]
trecho = ''
indice = 0

while True:
    if s[i] <= s[i + 1]:
        trecho = s[i]
        indice = i
        while (s[indice] <= s[indice+1]):
            trecho += s[indice+1]
            indice += 1
            if indice == len(s)-1:
                break

        i = indice +1

        if len(trechoG) < len(trecho):
            trechoG = trecho
    else:
        i +=1
    if i > len(s)-2:
        break
print('Longest substring in alphabetical order is: ' + str(trechoG))
