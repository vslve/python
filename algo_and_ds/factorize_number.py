def factorize_number(number):
    """Раскладывает число на множители"""
    
    divisor = 2
    while (number > 1):
        if (number % divisor == 0):
            print(divisor, end=" ")
            number /= divisor
        else:
            divisor += 1

factorize_number(int(input()))
