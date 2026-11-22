def binary_search(b, x):
    L = 0
    R = len(b) - 1

    while L < R:
        mid = (L + R + 1) // 2
        if b[mid] <= x:
            L = mid
        else:
            R = mid - 1

    return (L, b[L] == x)
