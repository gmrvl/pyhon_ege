file = open("24.33196.txt").read()

current_a = False # переменная, которая будет сообщать, прошлый символ == А или нет.

# если просят найти то, что встречается чаще всего - используем массив (список)
# ord() - конвертирует char в int (согласно ASCII кодировке)
# chr() - конвертирует int в char

letters = []

for i in range(300):
    letters.append(0)

for char in file:
    if current_a == True:
        letters[ord(char)] += 1
        current_a = False
    if char == 'A':
        current_a = True

max_letter = 0
max_index = 0
for i in range(300):
    if letters[i] > max_letter:
        max_letter = letters[i]
        max_index = chr(i)
print(max_index, max_letter)


# file = open("24.33196.txt").read()
#
# a = []
# for i in range(300):
#     a.append(0)
#
# current_a = 0
#
# for char in file:
#     if current_a == 1:
#         a[ord(char)] += 1
#         current_a = 0
#     if char == "A":
#         current_a = 1
#
# max_char = 0
# max_index = 0
#
# for i in range (300):
#     if a[i] > max_char:
#         max_char = a[i]
#         max_index = i
#
# max_index = chr(max_index)
# print(max_char, max_index)
