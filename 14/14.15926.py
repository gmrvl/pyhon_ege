a = 36 ** 7 + 6 ** 19 - 18
count = 0
while a != 0:
    if a % 6 == 0:
        count += 1
    a = a // 6
print(count)