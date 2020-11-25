def is_equal_strings(first_string:str, second_string:str):

    first_length = len(first_string)
    second_length = len(second_string)

    length = min(first_length, second_length)

    print(first_length, second_length)
    print(first_string, second_string)
    
    for i in range(length):
        first_char = first_string[i]
        second_char = second_string[i]
        if first_char != second_char or second_char == '*':
            if second_char == '*':
                i += 1
                k = i
                while (i < second_length and second_char == '*' ):
                    second_char = second_string[i]
                    i += 1
                if i == second_length:
                    return 'OK'
                if first_char == second_char:
                    return is_equal_strings(first_string[k - 1:], second_string[i - 1:])
                while (k < first_length and first_char != second_char):
                    first_char = first_string[k]
                    k += 1
                if k != first_length:
                    return is_equal_strings(first_string[k - 1:], second_string[i - 1:])
                return 'KO'
            if first_char != '*':
                k = i + 1
                second_char = second_string[0]
                while (k < first_length and first_char != second_char):
                    first_char = first_string[k]
                    k += 1
                if k != first_length:
                    return is_equal_strings(first_string[k - 1:], second_string)
                return 'KO'
            return 'KO'

    if second_length > length:
        for char in second_string[length:]:
            if char != '*':
                return 'KO'

    if first_length > length:
        return 'KO'

    return 'OK'


def main():

    if len(sys.argv) != 3:
        print("Введите две строки для сравнения в качестве аргументов командной строки, например: main.py 'a' 'a*'")
    else:
        print(is_equal_strings(sys.argv[1], sys.argv[2]))
    



if __name__ == '__main__':
    import sys

    main()
    
    
