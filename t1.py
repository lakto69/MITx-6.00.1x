import time

def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)

def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        print('1')
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)

L1 = []
L2 = [1]
L3 = [1, 2]
L4 = [6, 4, 9, 2]

t0 = time.clock()
swapSort(L4)
t1 = time.clock() - t0


t0 = time.clock()
swapSort(L4)
t2 = time.clock() - t0
print('modSwapSort(L4)', t1)
print('swapSort(L4)', t2)