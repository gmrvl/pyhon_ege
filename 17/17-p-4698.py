#  в которых хотя бы один из двух элементов больше, чем наибольшее из всех чисел в файле,делящихся на 127,
#   и в восьмеричной записи хотя бы одного элемента из двух содержится цепочка цифр 31.
#   В ответе запишите два числа: сначала количество найденных пар, а затем – минимальную сумму элементов таких пар.
#   В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

file = open('17-243.txt')

max127 = 0

for i in file:
    i = int(i)
    if i % 127 == 0 and i > max127:
        max127 = i

file.close()

file = open('17-243.txt')

count = 0
min_pair = 20001
last = int(file.readline())

for i in file:
    i = int(i)
    if last > max127 or i > max127:
        if oct(last).find('31') != -1 or oct(i).find('31') != -1:
            count += 1
            if last + i < min_pair:
                min_pair = last + i

    last = i

print(count, min_pair)


