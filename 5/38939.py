n = 0
while True:
    x = n
    digit_sum = 0
    position_sum = 0
    while x != 0:
        if (x % 10) % 2 == 0:
            digit_sum += x % 10
        x = x // 10
    x = str(n)
    for i in range(1, len(x), 2):
        position_sum += int(x[i])
    if digit_sum-position_sum == 13 or digit_sum-position_sum == -13:
        print(n)
        break

    n += 1
