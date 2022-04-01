def k(x, y):
    if x > y or y == 24:
        return 0
    elif x == y:
        return 1

    elif y % 2 != 0:
        return k(x, y - 1) + k(x, (y - 1) // 2)
    else:
        return k(x, y - 1)
print(k(1, 25))

