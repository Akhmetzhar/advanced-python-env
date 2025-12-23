def solve_equation():
    eq = input().strip() 

    a_val, op, b_val, _, c_val = eq[0], eq[1], eq[2], eq[3], eq[4]

    if a_val == 'x':
        b, c = int(b_val), int(c_val)
        if op == '+': result = c - b
        else: result = c + b
    elif b_val == 'x':
        a, c = int(a_val), int(c_val)
        if op == '+': result = c - a
        else: result = a - c
    else: 
        a, b = int(a_val), int(b_val)
        if op == '+': result = a + b
        else: result = a - b
        
    print(result)

if __name__ == "__main__":
    solve_equation()