file = open("33528.txt")

n = file.readline().split(" ")
a = []
b = []
money = int(n[1])

for i in file:
    s = i.split(" ")
    if s[2] == "A":
        a.append(s[0:2])
    else:
        b.append(s[0:2])

a = sorted(a)

print(a)