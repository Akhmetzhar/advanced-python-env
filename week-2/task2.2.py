def solve_cyclic_shifts():
    try:
        a = input().strip()
        b = input().strip()
    except EOFError:
        return

    if len(b) > len(a) or not b:
        print(0)
        return

    shifts = set()
    doubled_b = b + b
    for i in range(len(b)):
        shifts.add(doubled_b[i:i+len(b)])

    count = 0
    m = len(b)
    for i in range(len(a) - m + 1):
        if a[i:i+m] in shifts:
            count += 1
    
    print(count)

if __name__ == "__main__":
    solve_cyclic_shifts()