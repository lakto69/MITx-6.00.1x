# Função OK!
# def genPrimes():
#     x = 1
#     primo = []
#     while True:
#         x += 1
#         controle = True
#         for i in primo:
#             if x % i == 0:
#                 # Não é primo!
#                 controle = False
#                 break
#         if controle: # É primo!
#             primo.append(x)
#             yield primo


class genPrimes(object):
    def calcula():
        x = 1
        primo = []
        while True:
            x += 1
            controle = True
            for i in primo:
                if x % i == 0:
                    # Não é primo!
                    controle = False
                    break
            if controle: # É primo!
                primo.append(x)
                yield primo

    def __init__(self):
        print('--INIT---')
        self.primo = []
        self.x = 1
        print('primo:', self.primo, 'x:', self.x)
        # self.next()

    def __str__(self):
        print('--STR--')
        saida = ''
        for i in self.primo:
            print('for {} em {}'.format(i, self.primo))
            saida += str(i) + '\n'
            print('saida: ', saida)
        return saida

    def next(self):
        calcula()
        self.__next__

    # def next(self):
    #     print('NEXT...')
    #     while True:
    #         self.x += 1
    #         controle = True
    #         for i in self.primo:
    #             if self.x % i == 0:
    #                 # Não é primo!
    #                 controle = False
    #                 break
    #         if controle: # É primo!
    #             self.primo.append(self.x)
    #             yield self.primo

if __name__ == '__main__':
    a = genPrimes()
    print(a.next())