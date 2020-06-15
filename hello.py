def product(*, initial=1):
    total = initial
    yield
    for n in _:
        total *= n
    return total

choice

print( product(4, 5, 2, initial=3) )