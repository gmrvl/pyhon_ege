def K(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if y % 2 == 0:
        return K(x, y - 1) + K(x, y - 2) + K(x, y // 2)
    return K(x, y - 1) + K(x, y - 2)
print(K(3, 10)*K(10, 12))
