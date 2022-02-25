# #  Определите количество строк, в которых встречается комбинация A*R, где звёздочка обозначает любой символ.
# import re
# file = open('24-p-2558.txt')
#
# count = 0
# for string in file:
#     if len(re.findall('A.R', string)):
#         count += 1
# print(count)

file = open('24-p-2558.txt')
count = 0
for string in file:
    a = list(string)
    for i in range(len(a)-2):
        if a[i] == 'A' and a[i+2] == 'R':
            count += 1
            break
print(count)

