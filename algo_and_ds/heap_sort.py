from heap import Heap



def heapify(A:list):
    """Добавляет элементы списка в кучу. Возвращает получившуюся кучу.

       O(NlogN).

       O(N) - копирование элементов списка в кучу.
       
       O(logN) - сортировка элементов в куче глубиной H = logN.
    """

    heap = Heap()
    for x in A:
        heap.insert(x)
    return heap

def heapify_fast(A:list):
    """Добавляет элементы в кучу за О(N).

       Каждый родитель сравнивается по величине со своим потомком,
       меняясь или не меняясь позициями в соответствии с форматом кучи.
     
       Количество родителей в дереве: n / 2  с округлением вниз,
       количество листьев - n / 2 с округлением вверх,

       где n - количество элементов дерева.
       
    """
    
    heap = Heap()
    heap.values = [x for x in A] # помещаем в кучу неотсортированный список
    heap.size = len(A)
    for i in range(heap.size // 2, -1, -1):
        heap.sift_down(i)
    return heap

def get_sort_list(heap:list):
    """Извлекает корневой элемент из кучи в список, пока куча не пуста.
       Возвращает получившийся список.

       Список отсортирован по убыванию(возрастанию) в зависимости от формата кучи.
    """

    sorted_list = []
    while heap.size > 0:
        sorted_list.append(heap.extract_min())
    return sorted_list  
    

def heap_sort(A:list):
    """Сортирует массив используя сортировку кучей(пирамидальная сортировка)"""

    heap = heapify(A)
    sorted_list = get_sort_list(heap)
    for i in range(len(sorted_list)):
        A[i] = sorted_list[i]
    return A

def heap_sort_fast(A:list):
    """Сортирует массив используя сортировку кучей(пирамидальная сортировка)"""

    heap = heapify_fast(A)
    sorted_list = get_sort_list(heap)
    for i in range(len(sorted_list)):
        A[i] = sorted_list[i]
    return A


def test_heap_sort(sort_algorithm):
    A = [5, 7, 2, 1, 4, 3, 8, 10]
    A_sorted = [1, 2, 3, 4, 5, 7, 8, 10]
    print("testcase #1 -", "ok" if sort_algorithm(A) == A_sorted else "fail")

    A = [x for x in range(10, 0, -1)]
    A_sorted = [x for x in range(1, 11)]
    print("testcase #2 -", "ok" if sort_algorithm(A) == A_sorted else "fail")

    A = [x for x in range(10, 0, -1)] + [x for x in range(11, 17)] + [x for x in range(25, 16, -1)]
    A_sorted = [x for x in range(1, 26)]
    print("testcase #3 -", "ok" if sort_algorithm(A) == A_sorted else "fail")

def test_heap_sort_fast(sort_algorithm):
    A = [5, 7, 2, 1, 4, 3, 8, 10]
    A_sorted = [1, 2, 3, 4, 5, 7, 8, 10]
    print("testcase #1 -", "ok" if sort_algorithm(A) == A_sorted else "fail")

    A = [x for x in range(10, 0, -1)]
    A_sorted = [x for x in range(1, 11)]
    print("testcase #2 -", "ok" if sort_algorithm(A) == A_sorted else "fail")

    A = [x for x in range(10, 0, -1)] + [x for x in range(11, 17)] + [x for x in range(25, 16, -1)]
    A_sorted = [x for x in range(1, 26)]
    print("testcase #3 -", "ok" if sort_algorithm(A) == A_sorted else "fail")

test_heap_sort(heap_sort)
print()
test_heap_sort(heap_sort_fast)
