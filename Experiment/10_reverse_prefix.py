def reverse_prefix(b, n):
    left = 0
    right = n - 1

    while left < right:
        b[left], b[right] = b[right], b[left]
        left += 1
        right -= 1
