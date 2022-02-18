# для которых произведение элементов не кратно 14, затем максимальную из сумм элементов таких пар.

file = open("17.37347.txt")

count = 0

n2n7 = 0
n2 = 0
n7 = 0


for i in file:
    a = int(i)
    if a % 2 != 0 and a % 7 != 0:
        count += n2+n7+n2n7
        n2n7 += 1
    elif a % 2 == 0 and a % 7 != 0:
        count += n2n7+n7
        n7 += 1
    elif a % 2 != 0 and a % 7 == 0:
        count += n2n7+n2
        n2 += 1

print(count)