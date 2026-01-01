import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())
diag = float(input())

p1 = (a + b + diag) / 2
s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - diag))

p2 = (c + d + diag) / 2
s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - diag))

print(s1 + s2)
