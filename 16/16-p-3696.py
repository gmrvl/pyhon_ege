def F(n):
    if n <= 5:
        return n
    elif n > 5 and n % 5 == 0:
        return n + F(n/5 + 1)
    else:
        return n + F(n + 6)

for n in range(1, 100000):
    if n % 6 == 0 or n % 6 == 1:
        continue
    else:
        if F(n) > 1000:
            print(n)
            break
