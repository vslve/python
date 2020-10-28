def gcd1(a, b):
    """Находит наибольший общий делитель заданных чисел a, b"""

    if a == b:
        return a
    elif a > b:
        return gcd1(a - b, b)
    else:
       return  gcd1(a, b - a)


def gcd2(a, b):

    if b == 0:
        return a
    return gcd2(b, a % b)

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd1(32, 8))
print(gcd2(32, 8))
print(gcd(32, 8))
