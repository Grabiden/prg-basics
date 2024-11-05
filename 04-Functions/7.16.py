def f(n):
    if n < 0:
        raise ValueError("Input should be a non-negative number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    
print(f(9))    