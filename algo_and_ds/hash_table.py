def calc_hash(data):
    """Принимает последовательность произвольной длины,
       производит ее хэширование,возвращает хэш-сумму -
       битовую последовательность фиксированной длины.
    """

    k = 3571
    s = 0
    i = 1
    data = += 84832941
    while data > 0:
        s += data % 2 * k**i
        i += 1
        data //= 2
    return s % 2**8 # 8 хэщ-сумма 8 бит

class LinkedList():
    """Определяет связный список"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        """Добавляет элемент в список справа"""
        
        if not self.search(element):
            node = [element, None]
            if self.head is None:
                self.head = node
            else:
                self.tail[1] = node
            self.tail = node

    def search(self, element):
        """Осуществляет поиск элемента в списке.
           Если элемент найден - возвращает True, иначе - False.
        """

        curr = self.head
        while curr is not None:
            if curr[0] == element:
                return True
            curr = curr[1]
        return False

class HashTable():
    """Определяет хэш-таблицу открытой адрессации -
       массив связных списков, фиксированной размерности, где
       индекс каждого из связных списков соответствует хэш-сумме
       последовательности(элемента), помещаемой в данный список.
    """

    def __init__(self):
        self.table = [LinkedList() for i in range(256)] # 8 битная хэш-таблица

    def add(self, element):
        """Добавляет элемент в таблицу в соответствии с его хэш-суммой"""

        hsh = calc_hash(element)
        self.table[hsh].add(element)

    def search(self, element):
        """Осуществляет поиск элемента в таблице. O(1)"""

        hsh = calc_hash(element)
        return self.table[hsh].search(element)


    
