import math
#
# for i in range(1000000, 2000000):
#     count = 0  # количество разностей которые не превышает 100
#     stop = int(math.sqrt(i))
#     for d in range(1, stop):
#         if i % d == 0:
#             if i // d - d <= 100:
#                 count += 1
#                 if count >= 3:
#                     print(i)
#                     break


for i in range(1000000, 2000000):
    count = 0  # количество разностей которые не превышает 100
    stop = int(math.sqrt(i))
    first = True
    for d in range(stop, 0, -1):
        if i % d == 0:
            if i // d - d <= 100:
                count += 1
                if count >= 3:
                    print(i)
                    break
            elif first:
                print('False')
                break

            first = False
