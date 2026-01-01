import math

a = float(input())

triangle_area = (math.sqrt(3) / 4) * a * a
hexagon_area = 6 * triangle_area
print(hexagon_area)
