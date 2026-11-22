def pow2(n):
    if n < 0:
        return 0
    result = 1
    for i in range(n):
        result *= 2
    return result
