for i in range(0, 256):
    n = i
    np = bin(n)[2:]
    np = '0'*(8-len(np)) + np
    s = ''
    for d in np:
        if d == '1':
            s += '0'
        elif d == '0':
            s += '1'
    k = int(s, 2) - int(np, 2)
    if k == 111:
        print(n)
        break