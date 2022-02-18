a = []
count = 0
max_sum = 0
file = open("36000.txt")
n = int(file.readline())
for d in file:
    a.append(int(d))
# считаем пары, в которых разная четность & сумма есть в файле(массиве)
a = sorted(a)

for i in range(n):
    for j in range(i+1, n):
        if a[i] % 2 != a[j] % 2:
            current = a[i]+a[j]

            mid = len(a) // 2
            low = 0
            high = len(a) - 1

            while a[mid] != current and low <= high:
                if current > a[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                mid = (low + high) // 2

            if not low > high:
                count += 1
                if current > max_sum:
                    max_sum = current

print(count, "success", max_sum)
