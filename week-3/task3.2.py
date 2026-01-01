s = input()

words = s.split()
for w in words:
    letters = sorted(w)
    print("".join(letters), end=" ")
