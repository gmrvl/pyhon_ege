s = 4 ** 503 + 3 * 4 ** 244 - 2 * 4 ** 444 - 95

count = 0

while s != 0:
    if s % 4 == 3:
        count += 1
    s = s // 4
print(count)
