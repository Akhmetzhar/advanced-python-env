import math

a1 = float(input())
b1 = float(input())

a2 = float(input())
b2 = float(input())

h1 = math.sqrt(a1 * a1 + b1 * b1)
h2 = math.sqrt(a2 * a2 + b2 * b2)

print(h1)
print(h2)

if h1 > h2:
    print("first is greater")
elif h1 < h2:
    print("second is greater")
else:
    print("equal")
