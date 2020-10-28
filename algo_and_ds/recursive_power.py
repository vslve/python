def power(a, n):
    """Возведение числа a в сетпень n"""
    
    assert a != 0 , """Неккорректное число"""
    
    if n == 0:
        return 1
    elif  n % 2:
        return power(a**2, n // 2) * a
    else:
        return power(a, n - 1) * a

print(power(2, 10))
