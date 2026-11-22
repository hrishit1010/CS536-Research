def linear_search(b, n, x):
    for i in range(n):
        if b[i] == x:
            return i
    return n
