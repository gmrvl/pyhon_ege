for i in range(1, 10000):
    n = i
    b = bin(n)[2:]
    z = b
    b += b[-1]
    if z.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'

    f = bin(105)[2:]

    if len(b) >= len(f):
        if b > f:
            print(b)
            print(f)
            print(bin(111)[2:])
            break
