"""Cвязный список: [1, [2, [3, None]]] - первая позиция списка - ссылка на число,
       вторая позиция списка - ссылка на другой список, в котором первая позиция -
       ссылка на число, а вторая - на список и т.д. до None -
       признака окончания последовательности

       >>> a = [1]
       >>> a.append([2])
       >>> a[1].append([3, None])
       >>> p = a
       >>> while p != None:
               print(p[0])
               p = p[1]
       1
       2
       3
       
    """


class LinkedList():
    """Класс описывающи связный список.

       >>> A = LinkedList()
       >>> print(A.is_empty())
       True
       >>> A.insert(5)
       >>> print(A.is_empty())
       False
       >>> A.insert(10)
       >>> print(A.pop())
       10
       >>> print(A.is_empty())
       False
       >>> print(A.pop())
       5
       >>> print(A.is_empty())
       True

       """
    
    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not None, "List is empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x

    def is_empty(self):
        if self._begin == None:
            return True
        return False

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
