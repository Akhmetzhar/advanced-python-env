a = int(input())
op = input()
b = int(input())

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print("Division by zero!")
    else:
        print(a / b)