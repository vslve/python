class Heap():
    """Куча - структура данных, представляющая собой двоичное дерево,
       где в корне хранится наименьший(наибольший) элемент, а каждый
       потомок не меньше(не больше) своего родителя.

       Новые элементы добавляются в конец слева-направо.

       Пример: [x1, x2, x3, x4, x5, x6, x7, x8, x9, 10],

       где элементы 2*i + 1, 2*i + 2 - потомки текущего элемента,
       элемент (i - 1) // 2 - родитель.

       т.е. для x1(i = 0) - x2(i = 1) и x3(i = 2) - потомки.
            для x5(i = 4) и x6(i = 5) - родители x2 и x3 соответственно.

       >>> heap = Heap()
       >>> heap.insert(5)
       >>> heap.insert(2)
       >>> heap.insert(7)
       >>> heap.insert(1)
       >>> heap.insert(10)
       >>> print(heap.size, heap.values)
       5 [1, 2, 7, 5, 10]
       >>> print(heap.extract_min())
       1
       >>> print(heap.size, heap.extract_min())
       4 2
       >>> print(heap.size, heap.extract_min())
       3 5
       >>> print(heap.size, heap.extract_min())
       2 7
       >>> print(heap.size, heap.extract_min())
       1 10
       >>> print(heap.size)
       0
       >>> print(heap.extract_min())
       None

    """

    def __init__(self):
        self.values = []
        self.size = 0 # текущее кол-во элементов в кучу

    def insert(self, x):
        """Добавляет элемент x в кучу"""

        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)
        
    def sift_up(self, i):
        """Поднимает элемент на позицию, соответствующуу формату кучи:
           пока элемент не больше(не меньше) родителя.
        """
        
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def extract_min(self):
        """Извлекает минимальный элемент из кучи"""

        if not self.size:
            return None # куча пуста
        
        tmp = self.values[0]
        self.values[0] = self.values[self.size - 1] 
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return tmp

    def sift_down(self, i):
        """Опускает элемент на позицию, соответствующую формату кучи:
           пока элемент больше(меньше) потомка.
        """

        while 2 * i + 1 < self.size:
            j = i
            if self.values[i] > self.values[2 * i + 1]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[j] > self.values[2 * i + 2]:
                j = 2 * i + 2
            if i == j:
                break;
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j


if __name__ == "__main__":
    import doctest
    doctest.testmod()
