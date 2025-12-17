s = input() 

left_sum = int(s[0]) + int(s[1]) + int(s[2])

right_sum = int(s[3]) + int(s[4]) + int(s[5])

if left_sum == right_sum:
    print("YES")
else:
    print("NO")