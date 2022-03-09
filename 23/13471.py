def k(x, y):
    if x > y or y == 24:
        return 0
    if x == y:
        return 1
    if y % 2 != 0:
        return k(x, y - 1) + k(x, y - 1 // 2)
    return k(x, y - 1)
print(k(1, 3))

