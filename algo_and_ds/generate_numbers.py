def generate_numbers(N:int, M:int=-1, prefix=None):
    """Генерация всех чисел длинной M(по умолчанию M = N)
       от 0000...0 до NNNN...N, N < 10"""

    M = N if M == -1 else M
    prefix = prefix or []

    if M == 0:
        print(prefix)
        return
    for digit in range (N + 1):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()


generate_numbers(5, 3)
