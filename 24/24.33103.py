file = open("33103.txt")
count = 0
for line in file:
    if line.count('A') > line.count('E'): count += 1
print(count)
