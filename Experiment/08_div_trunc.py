def div_trunc(x, y):
    quotient = abs(x) // abs(y)

    if (x < 0) != (y < 0):
        return -quotient

    return quotient
