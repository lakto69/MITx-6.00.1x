def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


c = [9, 2, 8, 1, 5]

mySort(c)