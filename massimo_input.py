# questa versione sfrutta
# la gestione delle eccezioni
# per controllare l'uscita dal ciclo
# Per quanto possa sembrare strano, 
# in Python è un pattern piuttosto usato

m = None
while True:
    try:
        n = int(input())
        if not m or n > m:
            m = n
    except ValueError:
        break

print(m)
