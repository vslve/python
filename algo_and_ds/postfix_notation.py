

import stack

def postfix_notation(E:list):
    """Вычисляет выражение в постфиксной нотации(обратной польской нотации).

       >>> E = ['2', '7', '5', '*', '+']
       >>> postfix_notation(E) == 2 + 7 * 5
       True
       >>> E = ['2','5', '+', '7', '*']
       >>> postfix_notation(E) == (2 + 5) * 7
       True
    """
    
    for element in E:
        if element.isdigit():
            stack.push(element)
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            if element == '+':
                z = y + x
            elif element == '-':
                z = y - x
            elif element == '*':
                z = y * x
            else:
                z = y // x
            stack.push(z)
        
    result = stack.pop() 
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
