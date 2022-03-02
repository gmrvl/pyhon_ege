# #  Необходимо найти строку, содержащую наименьшее количество букв G
#
file = open('35482.txt')
min_string = file.readline()
min_count = min_string.count('G')
for i in file:
    if i.count('G') < min_count:
        min_count = i.count('G')
        min_string = i
print(min_string)
min_string = sorted(min_string)
min_string.pop(0)
letter = 0
count_l = 0
max_count_l = 0
last = 0

for i in min_string:
    if i == last or last == 0:
        count_l += 1
    else:
        if count_l >= max_count_l:
            max_count_l = count_l
            letter = last
        print(count_l, last)
        count_l = 1
    last = i
print(letter)

#  Ниже - правильная программа
# file = open('35482.txt')
#
# str = file.readline()
# c_G = str.count('G')
# for i in file:
#     if i.count('G') < c_G:
#         c_G = i.count('G')
#         str = i
#
# print(str)
#
# alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# a = []
#
# for i in range(len(alp)):
#     a.append(0)
#
# for s in str:
#     a[alp.find(s)] += 1
#
# max_count = max(a)
# print(max_count)
# for i in range(len(alp)):
#     if a[i] == max_count:
#         print(alp[i])
