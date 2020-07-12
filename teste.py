class genPrimes(object):

    def __init__(self):
        self.x = 2 #1
        self.primo = [2] #[]

    def __str__(self):
        saida = ''
        for i in self.next():
            saida += str(i) + '\n'
        return saida

    def next(self):
        print('x:', self.x, 'primo:', self.primo)
        while True:
            x += 1
            print('x:',x)
            controle = True
            for i in primo:
                if x % i == 0:
                    # Não é primo!
                    controle = False
                    break
            if controle: # É primo!
                primo.append(x)
                yield primo



a = genPrimes()
print(a)
a.next()