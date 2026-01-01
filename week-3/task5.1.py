def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input())
B = int(input())
C = int(input())
D = int(input())

num = A * D - C * B
den = B * D

g = gcd(abs(num), den)

num //= g
den //= g

print(num, "/", den)
