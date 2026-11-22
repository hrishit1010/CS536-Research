def common3(b0, b1, b2):
    k0 = k1 = k2 = 0
    n = len(b0)

    while k0 < n and k1 < n and k2 < n:
        if b0[k0] == b1[k1] == b2[k2]:
            return (k0, k1, k2)

        smallest = min(b0[k0], b1[k1], b2[k2])

        if b0[k0] == smallest:
            k0 += 1
        if b1[k1] == smallest:
            k1 += 1
        if b2[k2] == smallest:
            k2 += 1

    return None
