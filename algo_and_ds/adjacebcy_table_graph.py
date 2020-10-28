def make_graph():
    """Создает граф c N вершинами и M ребрами в виде
       таблицы смежности(списка списков).

       Получает два числа: N - кол-во вершин графа, M - кол-во ребер графа
       и M пар A B - имен ребер, где A, B - имена вершин ребра.

       Тест для графа

       5 5
       a b
       b c
       a d
       d e
       c a
       
       >>> graph = make_graph()
       >>> print(graph)
       [[0, 1, 1, 1, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 1, 0]]
    """

    N, M = [int(x) for x in input().split()]

    table = [[0] * N for i in range(N)]
    V = [] # список имен вершин графа
    index = {} # словарь соответствий индексов именам вершин
    for i in range(M):
        A, B = input().split() # имена вершин, образующих ребро
        for v in A, B:
            if v not in index:
                V.append(v)
                index[v] = len(V) - 1
        A_index = index[A] # индекс вершины A
        B_index = index[B] # индекс вершины B
        table[A_index][B_index] = 1
        table[B_index][A_index] = 1

    return table

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
