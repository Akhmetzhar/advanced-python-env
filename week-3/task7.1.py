def rect_area(a, b):
    return a * b

def tri_area(a, b):
    return a * b / 2

x = float(input())
y = float(input())
z = float(input())
t = float(input())

s = rect_area(x, y) + tri_area(z, t)
print(s)
