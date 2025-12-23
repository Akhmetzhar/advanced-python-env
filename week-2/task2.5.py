import re

def validate_license_plates():
    try:
        n_str = input().strip()
        if not n_str: return
        n = int(n_str)
    except EOFError:
        return

    allowed_letters = "ABCEHKMOPTXY"
    pattern = f'^[{allowed_letters}]\\d{{3}}[{allowed_letters}]{{2}}$'
    
    for _ in range(n):
        plate = input().strip()
        if re.match(pattern, plate):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    validate_license_plates()