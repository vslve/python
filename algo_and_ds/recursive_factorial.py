def recursive_factorial(n:int):
    """Вычисление факториала числа, используя рекурсию, n >= 0"""
    assert n >= 0, "Некорректное значение числа"
    if n == 1:
        return 1;
    return recursive_factorial(n-1) * n

print(recursive_factorial(5))
