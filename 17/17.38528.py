file = open('17-10.txt')
count = 0
k = int(file.readline())
min = 20001
for d in file:
    a = int(d)
    summ = k + a
    if 99 < summ < 1000:
        if summ % 10 > (summ % 100)//10:
            count += 1
            if summ < min:
                min = summ
    k = a

print(count, min)
