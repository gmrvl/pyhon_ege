file = open('27686.txt').read()

count = 0
max_count = 0

for char in file:
    if char == 'X':
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0

print(max_count)