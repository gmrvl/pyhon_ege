# Определите максимальное количество идущих подряд троек символов X*X или Y*Y, где * обозначает один любой символ.
#
# file = open('24-p-5042.txt').read()
#
# last = ''
# max_count = 0
#
# for char in file:
#     if len(last) % 3 == 0:
#         if ((char == 'X' or char == 'Y') and len(last) == 0) or ((char == 'X' or char == 'Y') and char == last[-1]):
#             last += char
#         else:
#             if len(last) > max_count:
#                 max_count = len(last)
#                 print(last)
#             last = ''
#     elif len(last) % 3 == 1:
#         last += char
#     elif len(last) % 3 == 2:
#         if char == last[-2]:
#             last += char
#         else:
#             if len(last) > max_count:
#                 max_count = len(last)
#                 print(last)
#             last = ''
# print(max_count)
# print(file.find(last))


file = open('24-p-5042.txt')
st = file.readline()

for i in range(1, len(st)):
    if st[i] == st[i+2]:
        pass
