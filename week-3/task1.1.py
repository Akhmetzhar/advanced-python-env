import math

shape = input()

if shape == "circle":
    r = float(input())
    print(math.pi * r * r)
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    print(a * b)
elif shape == "triangle":
    a = float(input())
    h = float(input())
    print(a * h / 2)
