def containsAny(str, set):
    for c in set:
        if c in str: return 1
    return 0

def containsAll(str, set):
    for c in set:
        if c not in str: return 0
    return 1
