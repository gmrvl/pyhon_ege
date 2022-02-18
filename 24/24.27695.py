file = open("24.27695.txt").read()

count = 0
max_count = 0

last = ''

for char in file:
    if char == last:
        if count > max_count:
            max_count = count
        count = 1
    else:
        count += 1
    last = char

print(max_count)
