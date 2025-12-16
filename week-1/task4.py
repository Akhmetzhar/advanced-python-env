import sys

N = int(sys.stdin.read().strip())
abs_N = abs(N)
S = abs_N * (abs_N + 1) // 2
print(S)