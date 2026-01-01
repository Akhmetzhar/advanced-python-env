m = int(input())
a = []

for i in range(m):
    a.append(int(input()))

print(a)

a[0], a[-1] = a[-1], a[0]

print(a)
