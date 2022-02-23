import math

for i in range(174457, 174506):
    deliteli = []
    stop = int(math.sqrt(i))
    for d in range(1, stop):
        if i % d == 0:
            deliteli.append(d)
            deliteli.append(i // d)
    if len(deliteli) == 4:
        print(deliteli)


# import math
#
# for i in range(174457, 174506):
#     a = []
#     stop = int(math.sqrt(i))
#     for j in range(1, stop):
#         if i % j == 0:
#             a.append(j)
#             a.append(i // j)
#         if len(a) > 4:
#             break
#     if len(a) == 4:
#         print(a[2], a[3])

