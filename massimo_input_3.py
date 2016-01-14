from sys import stdin
from itertools import takewhile

# Questa versione sfrutta il fatto che i files sono iteratori
# `takewhile` prende tutti gli elementi di una sequenza fino a quando
# il predicato è soddisfatto.

def condizione(x):
    return x != '\n'

lines = takewhile(condizione, stdin)

# Convertiamo in numeri, togliendo l'ultimo carattere ('\n') da ogni riga

numbers = [int(l[:-1]) for l in lines]

print(max(numbers))
