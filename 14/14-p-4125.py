a = 81**18 - (81**8 - 1)*((8 + 1)**8 + 1) / 8 - 8

count = 0

while a != 0:
    if a % 3 == 1:
        count += 1
    a = a // 3

print(count)
