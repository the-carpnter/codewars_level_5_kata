def zeros(n):
    return n//5 + zeros(n//5) if n else 0
