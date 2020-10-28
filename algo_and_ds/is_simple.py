def is_simple(number):
    """Проверяет число на простоту"""
    
    divisor = 2
    while (divisor < number):
        if number % divisor == 0:
            return False
        divisor += 1
    return True 

number = int(input())
print(is_simple(number))
