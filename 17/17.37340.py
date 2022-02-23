# разность которых четна
# хотя бы одно из чисел делится на 31

# у каких чисел разность будет четной? - оба четные либо оба нечетные
# что делать с числами, которые делятся\не делятся на 31

# если число четное и кратно 31, то его пары - все четные числа
# если число четное и не кратно 31, то его пары - все четные, кратные 31
# если число нечетное и кратно 31, то его пары - все нечетные числа
# если число нечетное и не кратно 31, то его пары - все нечетные, кратные 31

count = 0
maxs = -1

ch31 = 0
ch = 0
nch31 = 0
nch = 0

max_ch31 = 0
max_ch = 0
max_nch31 = 0
max_nch = 0

file = open("17.37340.txt")

for d in file:
    a = int(d)
    if a % 2 == 0 and a % 31 == 0:
        count += ch
        ch31 += 1
        ch += 1

        if a > max_ch31:
            max_ch31 = a
        elif a == max_ch31 and a > max_ch:
            max_ch = a

    elif a % 2 == 0 and a % 31 != 0:
        count += ch31
        ch += 1

        if a > max_ch:
            max_ch = a

    elif a % 2 != 0 and a % 31 == 0:
        count += nch
        nch31 += 1
        nch += 1

        if a > max_nch31:
            max_nch31 = a
        elif a == max_nch31 and a > max_nch:
            max_nch = a

    elif a % 2 != 0 and a % 31 != 0:
        count += nch31
        nch += 1

        if a > max_nch:
            max_nch = a

if max_ch31 + max_ch > max_nch31 + max_nch:
    maxs = max_ch31 + max_ch
else:
    maxs = max_nch31 + max_nch

print(count, maxs)

# если встретилось число, кратное 10, то его пары - любые числа
# если кратно 5, но не кратно 2, то его пары - числа, кратные 2
# если число кратно 2, но не кратно 5, то его пары - числа, кратные 5
# else (числа, не кратные 10, 5, 2), то его пары - числа, кратные 10
