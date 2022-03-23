for i in range(1, 10001):
    s = i
    n = 11
    while s > -9:
      s = s - 4
      n = n + 5
    if n == 56:
        print(i)