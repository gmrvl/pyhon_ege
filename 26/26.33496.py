a = []
count = 0
massa = 0
max_id = 0
file = open("33496.txt")
n = file.readline().split(" ")
for d in file:
    d = int(d)
    if 210 <= d <= 220:
        massa += d
        count += 1
    else:
        a.append(d)
a = sorted(a)

s = int(n[1])  # грузоподъемность грузовика
for i in range(len(a)):
    if massa + a[i] < s:
        massa += a[i]
        count += 1
    elif massa + a[i] == s:
        massa += a[i]
        count += 1
        max_id = i
        break
    elif massa + a[i] > s:
        max_id = i-1
        break

for j in range(max_id, 0, -1):
    if massa < s:
        massa -= a[j]
        for i in range(j+1, len(a)):
            if massa + a[i] == s:
                massa += a[i]
                max_id = i
                break
            elif massa + a[i] > s:
                massa += a[i-1]
                break
            elif massa + a[i] < s:
                continue
        else:
            break
print(massa, count)
