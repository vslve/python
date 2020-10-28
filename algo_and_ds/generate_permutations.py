def digit_in_prefix(digit, prefix):
    """Ищет число digit в списке чисел prefix
       Возвращает True, если число найдено,
       иначе - False
    """
    
    for element in prefix:
        if element == digit:
            return True
    return False

def generate_permutation(N:int, M:int=-1, prefix=None):
    """Генерация всех перестановок чисел от 1 до N в M позциях"""

    M = N if M == -1 else M
    prefix = prefix or []

    if M == 0:
        print(*prefix, sep="", end=" ")
        return
    for digit in range(1, N + 1):
        if digit_in_prefix(digit, prefix):
            continue
        prefix.append(digit)
        generate_permutation(N, M - 1, prefix)
        prefix.pop()

generate_permutation(5)
