file = open('35998.txt')
max_r = 0
for line in file:
    if line.count('A') < 25:
        for i in line:
            if line.rfind(i) - line.find(i) > max_r:
                max_r = line.rfind(i) - line.find(i)
print(max_r)
