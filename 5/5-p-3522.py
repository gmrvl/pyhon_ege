for i in range(1, 10000):
    n= i
    nb = bin(n)[2:]
    if n % 2 == 1:
        nb += '0'
    else:
        nb = '1'+nb
    if nb.count('1') % 2 == 0:
        nb += '1'
    else:
        nb += '0'

    s = bin(228)[2:]

    if len(nb) >= len(s):
        if nb > s:
            print(i)
            break