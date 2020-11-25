
def i_to_base(nb:int, base:str):
    digits_in_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    try:
        base = int(base)
    except:
        return f'"{base}"'
    else:
        if base >= 37 or base < 1:
            return f'"{base}"'
        if base == 0:
            return f'"0"'
        if base == 1:
            return '|' * nb
        if nb < base:
            return str(nb)
        
        based = [];
        while (nb >= base):
            digit = nb % base
            nb //= base
            if digit >= 10:          
                based.append(digits_in_letters[digit - 10])
            else:
                based.append(str(digit))
                
        if nb >= 10:          
            based.append(digits_in_letters[nb - 10])
        else:
            based.append(str(nb))
        return ''.join(based[::-1])

def i_to_base_all(nb:str, base_src:str, base_dst:str):
    allow_dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    try:
        base_src = int(base_src)
        base_dst = int(base_dst)
    except:
        return f'{nb} из "{base_src}" в "{base_dst}"'
    else:
        if base_src >= 37 or base_dst >= 37 or base_src < 1 or base_dst < 1:
            return f'{nb} из "{base_src}" в "{base_dst}"'
        if base_src == 1:
            return i_to_base(len(nb), base_dst)
        
        if nb.isdigit():
            for digit in nb:
                if int(digit) >= base_src:
                    return "Неверная базовая система счисления"
        else:
            for char in nb:
                if not char.isdigit() and char.upper() not in allow_dictionary:
                    return "Неверное число для перевода"
                char = int(char) if char.isdigit() else allow_dictionary.index(char.upper()) + 10
                if char >= base_src:
                    return "Неверная базовая система счисления"
                
        nb = list(nb)
        in_decimal = 0;
        power = 0
        while(nb):
            digit = nb.pop()
            digit = int(digit) if digit.isdigit() else allow_dictionary.index(digit.upper()) + 10
            in_decimal += digit * base_src **  power
            power += 1        
        return i_to_base(in_decimal, base_dst)
            

def main():

    usage = '\nДля перевода из десятичной системы счисления:\n\nвведите имя файла программы, десятичное число и целевую систему счисления в качестве аргументов командной строки, например:  main.py 15 5\n\nДля перевода из произвольной системы счисления:\n\nвведите имя файла программы, число, исходную и целевую систему счисления в качестве аргументов командной строки, например:  main.py 15 5 2\n'
    
    if 2 < len(sys.argv) < 5:
        if len(sys.argv) < 4:
            try:
                nb = int(sys.argv[1])
                base = sys.argv[2]
            except:
                print('\nНеверное число для перевода')
                print(usage)
            else:
                print(i_to_base(nb, base))
        else:
            print(i_to_base_all(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        print(usage)

        
            
            
if __name__ == '__main__':
    
    import sys
    
    main()
    
