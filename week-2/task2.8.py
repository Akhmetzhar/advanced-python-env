import sys

def check_anagram():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return

    s1 = input_data[0]
    s2 = input_data[1]

    if len(s1) != len(s2):
        print("NO")
        return

    if sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    check_anagram()