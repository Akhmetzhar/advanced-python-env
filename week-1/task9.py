ticket = input()
print("YES" if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])) else "NO")
