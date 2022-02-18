file = open('37337.txt')

count = 0
max_s = 0
m_1 = 0  # максимумы, не кратные 7
m_2 = 0
m7_1 = 0  # максимумы, кратные 7
m7_2 = 0
m7_3 = 0

a = []  # хранятся КОЛИЧЕСТВА чисел, остатки от деления на 160 которых равны индексу
count_a = 0  # количество чисел, которые мы записали в этот массив (не 160, а количество чисел, которые мы уже прочли из файла и записали в этот массив)
a7 = []
count_a7 = 0

for i in range(160):
    a.append(0)
    a7.append(0)

for d in file:
    d = int(d)
    ost = d % 160
    if d % 7 == 0:
        count += count_a + count_a7
        count -= (a7[ost] + a[ost])
        a7[ost] += 1
        count_a7 += 1

        if d > m7_1:
            m7_1 = d
        elif d > m7_2:
            m7_2 = d
        elif d > m7_3:
            m7_3 = d
    else:
        count += count_a7
        count -= a7[ost]
        a[ost] += 1
        count_a += 1

        if d > m_1:
            m_1 = d
        elif d > m_2:
            m_2 = d

# if m_1 > m7_1 and m_1 % 160 != m7_1 % 160:
#     max_s = m_1 + m7_1
# elif m_1 > m7_2 and m_1 % 160 != m7_1 % 160:
#     max_s = m_1 + m7_1
# elif m_1 > m7_2 and m_1 % 160 != m7_1 % 160:
#     max_s = m_1 + m7_1
# elif m_1 > m7_2 and m_1 % 160 != m7_1 % 160:
#     max_s = m_1 + m7_1
if m_1 > m7_2:
    max_s = m_1 + m7_1
else:
    max_s = m7_1 + m7_2

print(count, max_s)
