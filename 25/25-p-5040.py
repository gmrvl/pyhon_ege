for i in range(0, 10):
    d_str = '3' + str(i) + '4583'
    d = int(d_str)
    last = 0
    summ = 0
    nine = ''
    while d != 0:
        nine = str(d % 9) + nine
        d = d // 9
    ok = True
    for k in range(0, len(nine) - 1):
        if nine[k] < nine[k + 1]:
            ok = False
    if ok:
        for a in range(len(nine)):
            summ += int(nine[a])
        print(d_str, summ)

for i in range(0, 10):
    for j in range(0, 1000):
        d_str = '3' + str(i) + '458' + str(j) + '3'
        d = int(d_str)
        last = 0
        summ = 0
        nine = ''
        while d != 0:
            nine = str(d % 9) + nine
            d = d // 9
        ok = True
        for k in range(0, len(nine)-1):
            if nine[k] < nine[k+1]:
                ok = False
        if ok:
            for a in range(len(nine)):
                summ += int(nine[a])
            print(d_str, summ)

