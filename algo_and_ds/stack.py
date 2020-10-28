


"""
Модуль, описывающий структуру данных стек.

>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True

"""

_stack = []

def push(x):
    """Добавляет элемент x в конец стека.

       >>> size = len(_stack)
       >>> push(5)
       >>> len(_stack) - size
       1
       >>> _stack[-1]
       5

    """
    
    _stack.append(x)

def pop():
    x = _stack.pop()
    return x

def is_empty():
    return len(_stack) == 0

def clear():
    _stack.clear()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)


