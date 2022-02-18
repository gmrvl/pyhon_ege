# быстрый и эффективный алгоритм поиска количества делителей

# def fact(a):
#     i = 1
#     o = 0
#     while i * i <= a:
#         if a % i == 0 and i * i != a:
#             o += 2
#         elif a % i == 0 and i * i == a:
#             o += 1
#         i += 1
#     return o


# тупой перебор
import math

for digit in range(35000000, 40000001):
    count = 0
    stop = round(math.sqrt(digit))
    for i in range(1, stop):
        if digit % i == 0:
            if i % 2 == 1:
                count += 1
            second = digit / i
            if second%2 == 1 and second != i:
                count += 1
        if count > 5:
            break
    print(digit)
    if count == 5:
        print(digit, count, "YOU WIN")
