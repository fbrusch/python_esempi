# Questa versione invece si aspetta che la lista di numeri
# sia terminata da un EOF (ctrl-d).


import sys

# Leggo tutto lo stdin, lo spezzo in linee
# e lo metto in lines

lines = sys.stdin.read().split()

# converto in numeri

numbers = [int(l) for l in lines]

# stampo il massimo

print(max(numbers))
