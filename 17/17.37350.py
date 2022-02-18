# количество пар элементов последовательности, у которых сумма нечётна,
# а произведение делится на 3, затем максимальную из сумм элементов таких пар

file = open("17.37350.txt")

max_sum = 0
count = 0  # счетчик ПАР

# для каждого четного числа, кратного 3 - нечетное
# для каждого нечетного пара, кратного 3 - четное
# для каждого четного числа, не кратного 3 - нечетные, кратные 3
# для каждого нечетного пара, не кратного 3 - четное, кратное 3

ch_3 = 0
nch_3 = 0
ch_n3 = 0
nch_n3 = 0

max_ch_3 = 0
max_nch_3 = 0
max_ch_n3 = 0
max_nch_n3 = 0


for i in file:
    a = int(i)
    if a % 2 == 0 and a % 3 == 0:
        count += nch_3
        count += nch_n3
        ch_3 += 1
        if a > max_ch_3:
            max_ch_3 = a
    elif a % 2 == 1 and a % 3 == 0:
        count += ch_3
        count += ch_n3
        nch_3 += 1
        if a > max_nch_3:
            max_nch_3 = a
    elif a % 2 == 0 and a % 3 != 0:
        count += nch_3
        ch_n3 += 1
        if a > max_ch_n3:
            max_ch_n3 = a
    elif a % 2 == 1 and a % 3 != 0:
        count += ch_3
        nch_n3 += 1
        if a > max_nch_n3:
            max_nch_n3 = a

first_sum = max_ch_3 + max_nch_3
second_sum = max_ch_3 + max_nch_n3
third_sum = max_nch_3 + max_ch_n3

if first_sum > second_sum:
    max_sum = first_sum
else:
    max_sum = second_sum
if third_sum > max_sum:
    max_sum = third_sum


print(count, max_sum)



