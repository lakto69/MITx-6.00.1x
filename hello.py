# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:53:38 2020

@author: leite.aml
"""
#   '0123456789012345678901234567890
s = 'código alterado'
print('s:', len(s))

trechoG = s[0]
trecho = ''

for i in range(len(s)-1):
    print('-i:',i)

    if s[i] <= s[i + 1]:
        trecho = s[i]
        print('while:',i)
        while (s[i] <= s[i+1]):
            trecho += s[i+1]
            i += 1
            print('--',i)
            if i == len(s)-1:
                break

        print('trecho:',trecho)
        print('i:',i)

        if len(trechoG) < len(trecho):
            trechoG = trecho
            print('trechoG:', trechoG)
    else:
        print('i:',i)
print('Longest substring in alphabetical order is: ' + str(trechoG))
