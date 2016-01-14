# leggi da tastiera una sequenza di numeri
# terminata da input vuodo (solo 'enter')
# e stampa il massimo

_str = input()
_max = None
while not _str == '':
    _n = int(_str)
    if not _max or _n > _max:
        _max = _n
    _str = input()

print(_max)




