import stack

def is_braces_sequence_correct(s:str):
    """Проверяет является ли корректной скобочная последовательность,
       содержащая скобки вида: () [].

       >>> is_braces_sequence_correct("(([()]))[]")
       True
       >>> is_braces_sequence_correct("([)]")
       False
       >>> is_braces_sequence_correct("(")
       False
       >>> is_braces_sequence_correct("]")
       False
       
    """

    for brace in s:
        if brace not in "[]()":
            continue
        if brace in "[(":
            stack.push(brace)
        else:
            assert brace in ")]" , "Ожидалась закрывющая скобка, получена: " + str(brace)
            if stack.is_empty():
                return False
            left = stack.pop()
            assert left in "([" "Ожидалась открывающая скобка, получена: " + str(brace)
            if left == "(":
                right = ")"
            else:
                right = "]"
            if brace != right:
                return False
    return stack.is_empty()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
