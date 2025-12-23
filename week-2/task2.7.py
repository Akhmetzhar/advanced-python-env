from collections import Counter

def analyze_shopping_list():
    try:
        data = input().split()
    except EOFError:
        return

    if not data: return

    counts = Counter(data)
    
    print("Purchase frequency:")
    for item in sorted(counts.keys()):
        print(f"{item}: {counts[item]}")
        
    most_popular = counts.most_common(1)[0][0]
    print(f"Most popular item: {most_popular}")
    
    once = [item for item, count in counts.items() if count == 1]
    print(f"Purchased once: {' '.join(sorted(once))}")
    
    print("Sorted by frequency:")
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for item, count in sorted_items:
        print(f"{item} {count}")

if __name__ == "__main__":
    analyze_shopping_list()