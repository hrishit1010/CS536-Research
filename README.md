# Evaluation of an LLM in Generating Python Code Using Formal Verification Concepts

Course project for CS-536 *Science of Programming* (Fall 2026).
Section: 03
Professor: Dr. Xiaolong Wang
Essay
## About

This project checks whether an LLM writes Python programs that are correct under the standards of the Science of Programming: Hoare triples, loop invariants, bound functions and total correctness.

Ten programming tasks were given to the model as short prompts that never mentioned testing. The generated programs were then verified by hand with formal proof techniques.

**Model used:** gpt-6

## The ten tasks

| # | Function | Precondition | Postcondition |
| --- | --- | --- | --- |
| 1 | `sum_to(n)` | n >= 0 | result = 0 + 1 + ... + n |
| 2 | `pow2(n)` | none | 2^n if n >= 0, else 0 |
| 3 | `gcd(a, b)` | a > 0, b > 0 | greatest common divisor |
| 4 | `linear_search(b, n, x)` | 0 <= n <= size(b) | leftmost index of x, or n |
| 5 | `binary_search(b, x)` | b strictly increasing, non-empty, b[0] <= x <= b[-1] | L with b[L] <= x < b[L+1]; found iff b[L] = x |
| 6 | `swap(b, m, n)` | indices in range | b[m] and b[n] exchanged |
| 7 | `common3(b0, b1, b2)` | sorted, equal length | indices of a common value, or None |
| 8 | `div_trunc(x, y)` | y != 0 | x / y truncated toward 0 |
| 9 | `isqrt(n)` | n >= 0 | r with r^2 <= n < (r+1)^2 |
| 10 | `reverse_prefix(b, n)` | 0 <= n <= size(b) | first n elements reversed in place |

## Prompts and generated code

### 1. Sum

**Prompt**

> Write a Python function sum_to(n) that returns 0 + 1 + 2 + ... + n. You may assume n is an integer and n ≥ 0. Return only the code.

**Generated code**

```python
def sum_to(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
```

### 2. Power of 2

**Prompt**

> Write a Python function pow2(n) that returns 2 to the power n if n ≥ 0, and returns 0 if n < 0. Do not use the ** operator or pow. Return only the code.

**Generated code**

```python
def pow2(n):
    if n < 0:
        return 0
    result = 1
    for i in range(n):
        result *= 2
    return result
```

### 3. GCD by repeated subtraction

**Prompt**

> Write a Python function gcd(a, b) that returns the greatest common divisor of a and b using Euclid's subtraction method (replace the larger number by the difference). You may assume a and b are positive integers. Return only the code.

**Generated code**

```python
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
```

### 4. Linear search

**Prompt**

> Write a Python function linear_search(b, n, x) that looks at the first n elements of list b and returns the index of the leftmost occurrence of x among them, or n if x does not occur among them. You may assume 0 ≤ n ≤ len(b). Return only the code.

**Generated code**

```python
def linear_search(b, n, x):
    for i in range(n):
        if b[i] == x:
            return i
    return n
```

### 5. Binary search

**Prompt**

> Write a Python function binary_search(b, x) that returns a pair (L, found). L is the index such that b[L] ≤ x, and either L is the last index or x < b[L+1]. found is True exactly when b[L] == x. You may assume b is non-empty, strictly increasing, and b[0] ≤ x ≤ b[-1]. Return only the code.

**Generated code**

```python
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
```

### 6. Swap in an array

**Prompt**

> Write a Python function swap(b, m, n) that swaps the values at positions m and n of list b in place. You may assume 0 ≤ m < len(b) and 0 ≤ n < len(b). Return only the code.

**Generated code**

```python
def swap(b, m, n):
    temp = b[m]
    b[m] = b[n]
    b[n] = temp
```

### 7. Common element of three sorted arrays

**Prompt**

> Write a Python function common3(b0, b1, b2) that returns indices (k0, k1, k2) with b0[k0] == b1[k1] == b2[k2], or None if no such indices exist. Use three pointers that only move forward. You may assume the three lists have the same length n and are sorted in non-decreasing order. Return only the code.

**Generated code**

```python
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
```

### 8. Division rounding toward zero

**Prompt**

> Write a Python function div_trunc(x, y) that returns the integer quotient of x divided by y, rounded toward zero. For example 13 / 3 = 4, 13 / (-3) = -4, and (-13) / 3 = -4. You may assume y ≠ 0. Do not use int(x / y). Return only the code.

**Generated code**

```python
def div_trunc(x, y):
    quotient = abs(x) // abs(y)
    if (x < 0) != (y < 0):
        return -quotient
    return quotient
```

### 9. Integer square root

**Prompt**

> Write a Python function isqrt(n) that returns the largest integer r such that r * r ≤ n. Do not use math.sqrt, math.isqrt or **0.5. You may assume n is an integer and n ≥ 0. Return only the code.

**Generated code**

```python
def isqrt(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            low = mid + 1
        else:
            high = mid - 1
    return high
```

### 10. Reverse a prefix in place

**Prompt**

> Write a Python function reverse_prefix(b, n) that reverses the first n elements of list b in place, leaving the rest unchanged. You may assume 0 ≤ n ≤ len(b). Return only the code.

**Generated code**

```python
def reverse_prefix(b, n):
    left = 0
    right = n - 1
    while left < right:
        b[left], b[right] = b[right], b[left]
        left += 1
        right -= 1
```

## Method

1. A specification (precondition and postcondition) was fixed for each task.
2. Each task was given to the model as a plain prompt.
3. Each program was verified by hand. For every loop the following were checked: the invariant holds on entry, is preserved, implies the postcondition on exit, the bound function decreases, and no runtime error occurs.
4. Behaviour on inputs outside the precondition was also traced, to see which condition protects each program.

## Result

All ten programs were proved totally correct under their stated preconditions. Outside the precondition the programs have no guards: `gcd(0, 5)` loops forever, `isqrt(-5)` returns -5, and several functions raise `IndexError` or `ZeroDivisionError`. Under total correctness these inputs are not covered by the specification.

## AI assistance

*AI was used only to generate code for experimental purpose only as per the essay requirement.The result were manually verified and analysed*

## Limitations

- One model, ten tasks and one answer per task, so the results describe this sample only.
- The tasks are classic textbook problems.
- The proofs were checked by hand, not by any AI Tools.
