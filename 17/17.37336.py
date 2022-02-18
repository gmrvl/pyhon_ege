count = 0  # счетчик чего-то
max_sum = -20_000
last = None

file = open("37336.txt")

for d in file:  # d - это наши цифры
    a = int(d)
    if a % 3 == 0:
        if last % 3 == 0:
            count += 1
        else:
            count += 2
    if (last != None) and (a + last > max_sum):
        max_sum = a + last
    last = a

if last % 3 == 0:
    count -= 1
print(count, max_sum)
