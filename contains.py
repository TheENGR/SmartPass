def containsAny(a, b):
    for c in b:
        if c in a: return 1
    return 0

def containsAll(a, b):
    for c in b:
        if c not in a: return 0
    return 1

def arrayContains(a, b):
    return [c in a for c in b]
