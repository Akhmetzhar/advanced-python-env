def all_eq(lst):
    if not lst:
        return []

    max_len = max(len(s) for s in lst)

    result = [s.ljust(max_len, '_') for s in lst]
    return result
