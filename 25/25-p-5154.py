if 159 % 21 == 0:
    a = 159 // 21
    print(159, a)

for i in range(2, 235):
    if i < 5 or i == 23 or i == 24 or i == 34 or i == 234:
        d = '1' + str(i) + '59'
        if int(d) % 21 == 0:
            n = int(d) // 21
            print(d, n)

for i in range(6, 679):
    if i < 9 or i == 67 or i == 68 or i == 78 or i == 678:
        d = '15' + str(i) + '9'
        if int(d) % 21 == 0:
            n = int(d) // 21
            print(d, n)

for i in range(2, 235):
    for j in range(6, 679):
        if i < 5 or i == 23 or i == 24 or i == 34 or i == 234:
            if j < 9 or j == 67 or j == 68 or j == 78 or j == 678:
                d = '1' + str(i) + '5' + str(j) + '9'
                if int(d) % 21 == 0:
                    n = int(d) // 21
                    print(d, n)



# d = '1'
# for a in range(2, 5):
#     d += str(a)
#     for b in range(3, 5):
#         if b > a:
#             d += str(b)
#         else:
#             break
#         for c in range(4, 5):
#             if c > b:
#                 d += str(c)
#             else:
#                 break
#     d += '59'
#     if int(d) % 21 == 0:
#         n = int(d) // 21
#         print(d, n)
#     d = d[:-1]
#     for e in range(6, 9):
#         d += str(e)
#         for f in range(7, 9):
#             if f > e:
#                 d += str(e)
#             else:
#                 break

# for i in range(2, 235):
#     last = 10
#     ok = True
#     while i > 0:
#         if i % 10 > last:
#             ok = False
#             break
#         last = i % 10
#         i = i // 10
#     if ok:
#         d = '1' + str(i)