def inside(x, y, r):
    return x * x + y * y <= r * r

r = float(input())

count = 0

x = float(input())
y = float(input())
if inside(x, y, r):
    count += 1

x = float(input())
y = float(input())
if inside(x, y, r):
    count += 1

x = float(input())
y = float(input())
if inside(x, y, r):
    count += 1

print(count)
