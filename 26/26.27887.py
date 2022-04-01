file = open('27887.txt')
arr = []
first = file.readline().split(' ')
s = int(first[0])
n = int(first[1])
for i in file:
    i = int(i)
    arr.append(i)
arr = sorted(arr)

a_sum = 0
count = 0
for i in arr:
    if a_sum + i <= s:
        a_sum += i
        count += 1
    else:
        break
a_sum -= arr[count-1]  # из массива достаем последний элемент, который попал в нашу сумму (count - 1, потому что индекс начинается с 0)
max_a = arr[count-1]
for i in range(count, n):
    if a_sum + arr[i] <= s:
        max_a = arr[i]
    else:
        break

print(count, max_a)
