def make_graph():
    """Создает граф с N вершинами и M ребрами
       в виде списков смежности: A : B, C, D, E...,
       где B, C, D, E... - имена вершин соседних с вершиной A.

       Получает два числа: N - кол-во вершин графа, M - кол-во ребер графа и
       M пар имен ребер вида A B, где A и B - имена вершин, образующих ребро.

       Тест графа:

       5 5
       a b
       b c
       a d
       d e
       c a
       
       >>> graph = make_graph()
       >>> graph == {'a': {'d', 'c', 'b'}, 'b': {'a', 'c'}, 'c': {'a', 'b'}, 'd': {'a', 'e'}, 'e': {'d'}}
       True
    """

    N, M = [int(x) for x in input().split()]

    graph = {} # словарь соответсвий имени вершины и ее соседей

    for edge in range(M):
        A, B = input().split()
        for v1, v2 in (A, B), (B, A):
            if v1 not in graph:
                graph[v1] = {v2}
            else:
                graph[v1].add(v2)

    return graph

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
