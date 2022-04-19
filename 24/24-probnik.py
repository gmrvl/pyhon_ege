# найти самую длинную подстроку, в которой нет комбинации KL и LK

file = open('33196.txt').read()

count = 0
max_count = 0
last = None
for i in file:
    if i == "K":
        if last == "L":
            if count > max_count:
                max_count = count
            count = 1
        else:
            count += 1
    elif i == "L":
        if last == "K":
            if count > max_count:
                max_count = count
            count = 1
        else:
            count += 1
    else:
        count += 1
    if count > max_count:
        max_count = count
    last = i
print(max_count)