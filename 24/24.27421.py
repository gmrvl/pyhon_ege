#  Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

file = open('27421.txt').read()

count = 0  # сколько символов идущих подряд удовлетворяют условию (длина цепочки)
max_count = 0  # максимальная длина цепочки

last = 0
for i in file:
    if i == last:
        if max_count < count:
            max_count = count
        count = 1
    else:
        count += 1

    last = i

if max_count < count:
    max_count = count

print(max_count)
