import math

n = 4679000
count = 0

while True:
    n += 1
    a = []
    b = []
    stop = int(math.sqrt(n))
    result = ''

    for dell in range(2, stop):
        if n % dell == 0:
            a.append(dell)
            a.append(n // dell)
    a = sorted(a)
    for dell in a:
        ok = True
        stop_dell = int(math.sqrt(dell))
        for j in range(2, stop_dell):
            if dell % j == 0:
                ok = False
                break
        if ok:
            result += str(dell)
            b.append(dell)
    if result[0:2] == '27' and result[-3:-1] == '39':
        print(n, b[len(b)-1])
        count += 1
    if result[0:2] == '34' and result[-3] == '2' and result[-1] == '7':
        print(n, b[len(b)-1])
        count += 1
    if count > 4:
        break
