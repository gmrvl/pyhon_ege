file = open("27423.txt")

n = file.readline().split(" ")
disk = int(n[0])
a = []
current_sum = 0
count = 0
max_file = 0
for d in file:
    a.append(int(d))

a = sorted(a)

for i in range(len(a)):
    if disk - current_sum >= a[i]:
        current_sum += a[i]
        count += 1
        max_file = a[i]

if disk - current_sum > 0:
    current_sum -= a[count-1]
    for i in range(count, len(a)):
        if disk - current_sum < a[i]:
            max_file = a[i-1]
            break
        elif disk - current_sum == a[i]:
            max_file = a[i]
            break
        else:
            continue

print(count, max_file)
