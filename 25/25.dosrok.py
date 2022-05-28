for i in range(0, 10):
    a = '12345' + str(i) + '6'
    for j in range(0, 10):
        b = int(a + str(j) + '8')
        if b % 17 == 0:
            print(b, b//17)