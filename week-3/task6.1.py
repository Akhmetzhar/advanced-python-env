def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())

g = gcd(a, b)
l = a * b // g

print(g)
print(l)
