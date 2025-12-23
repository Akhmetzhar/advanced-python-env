def count_unique_words():
    line1 = input().split()
    if not line1: return
    n, m = map(int, line1)
    text = input().strip()
    
    unique_words = set()
    for i in range(len(text) - m + 1):
        unique_words.add(text[i:i+m])
        
    print(len(unique_words))

if __name__ == "__main__":
    count_unique_words()