

def sequencia(texto, indice, trechoG):
    trecho = texto[indice]
    while texto[indice] <= texto[indice+1]:
        trecho += texto[indice+1]
        indice += 1
    if len(texto)-1 > 1: #indice < len(texto)-1:
        return sequencia(texto[indice+1:], 0, trecho)
    else:
        if len(trechoG) < len(trecho):
            trechoG = trecho
        return trechoG

s = input('Digite a cadeia de caracteres:') #'zydjrwcyjslqgypl'
print(sequencia(s, 0, ''))