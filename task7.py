a=int(input())
op=input()
b=int(input())

print(a+b if op=='+' else a-b if op=='-' else a*b if op=='*' else "Division by zero" if b==0 else a//b)
