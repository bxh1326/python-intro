def max_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c
print(max_number(12, 12, 9))
print(max_number(12, 12, 3))
