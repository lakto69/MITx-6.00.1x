
def oddTuples(*aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    oList = []
    for t in aTup[::2]:
        oList.append(t)

    return tuple(oList)

# print(oddTuples('I', 'am', 'a', 'test', 'tuple'))

""" apply to each 1"""
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

# def timesFive(a):
#     return a * 5
# applyToEach(testList, timesFive)

# def minhafuncao(a):
#     return a ** 2
# applyToEach(testList, minhafuncao)

# print(testList)

""" EXERCÍCIO 5"""
def applyEachTo(L, x):
    result = []
    for i in L:#range(len(L)):
        result.append(i(x))#L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

# print(applyEachTo([inc, square, halve, abs], 3.0))

texto = """
In computer science, string interning is a method of storing only one copy of each distinct string value, which must be immutable.[1] Interning strings makes some string processing tasks more time- or space-efficient at the cost of requiring more time when the string is created or interned. The distinct values are stored in a string intern pool.
The single copy of each string is called its intern and is typically looked up by a method of the string class, for example String.intern()[2] in Java. All compile-time constant strings in Java are automatically interned using this method.[3]
String interning is supported by some modern object-oriented programming languages, including Java, Python, PHP (since 5.4), Lua,[4] Ruby (with its symbols), Julia and .NET languages.[5] Lisp, Scheme, and Smalltalk are among the languages with a symbol type that are basically interned strings. The library of the Standard ML of New Jersey contains an atom type that does the same thing. Objective-C's selectors, which are mainly used as method names, are interned strings.
Objects other than strings can be interned. For example, in Java, when primitive values are boxed into a wrapper object, certain values (any boolean, any byte, any char from 0 to 127, and any short or int between −128 and 127) are interned, and any two boxing conversions of one of these values are guaranteed to result in the same object.[6]
"""
def lyrics_to_freq(lyrics):
    myDict = {}
    for word in lyrics.lower().split():
        if word.isalpha():
            if word in myDict:
                myDict[word] += 1
            else:
                myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

# print(words_often(texto, 5))

# print(words_often(lyrics_to_freq(texto),2))

"""Exercise: how many """

animals = {
 'a': ['aardvark'],
 'b': ['baboon'],
 'c': ['coati'],
 'd': ['donkey', 'dog', 'dingo']}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    qtde=0
    for valor in aDict.values():
        qtde += len(valor)
    return qtde

# print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    qtde, quem =0, ''
    for valor in aDict:
        # print(valor, aDict[valor])
        if len(aDict[valor]) > qtde:
            qtde, quem = len(aDict[valor]), valor
            # print(qtde, aDict[valor])
    if qtde > 0:
        return quem
# print(biggest({'a': [], 'b': []}))

# def biggest_c(aDict):
#     return max(map(lambda x: (len(x[1]), x[0]), aDict.items()))[1]
#     # OU:
#     return max((len(aDict[k]), k) for k in aDict)[1]

# print(biggest_c({'b': [], 'a': []}))

