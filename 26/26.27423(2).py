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
print(a)

for i in range(len(a)-1):
    if disk - current_sum == a[i]:
        current_sum += a[i]
        count += 1
        break
    elif disk - current_sum > a[i]:
        current_sum += a[i]
        count += 1
    elif disk - current_sum < a[i]:
        current_sum -= a[i-1]
        j = i
        while disk - current_sum > a[j]:
            max_file = a[j]
            j += 1

print(count, max_file)
