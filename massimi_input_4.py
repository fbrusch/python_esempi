# Prende in ingresso una sequenza di numeri, terminata da un '\n'
# Il primo chiamiamolo n, gli altri 'resto'
# Alla fine, stampa gli n numeri più grandi in resto 

from sys import stdin
from itertools import takewhile

n = int(stdin.readline().rstrip('\n'))

lines = takewhile(lambda x: x != '\n', stdin)

lines = [int(l.rstrip('\n')) for l in lines]

for l in lines[-n:]:
    print(l)
