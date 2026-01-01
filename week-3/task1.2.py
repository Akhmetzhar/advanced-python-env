for i in range(3):
    arr = list(map(int, input().split()))
    s = sum(arr)
    avg = s / len(arr)
    print(s, avg)
