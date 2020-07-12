def genPrimes():
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
            yield x #str(primo[-1]) #+ '\n'

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

a = genPrimes()

