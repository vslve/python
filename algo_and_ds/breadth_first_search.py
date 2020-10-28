def make_graph(N, M):
    """Создает граф из N вершин и M ребер в виде словаря:

       {вершина : {множество соседних вершин}}
    """

    graph = {i:set() for i in range(N)}
    for i in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].add(v2)
        graph[v2].add(v1)

    return graph

def bfs_distances(start_vertex, graph=None):
    """Выполняет обход графа в ширину.
       Подсчитывает расстояние до каждой вершины
       от вершины старта start_vertex.

       Тест для графа 15 вершин, 16 ребер:

       0 1
       0 12 
       0 11
       0 10
       2 6
       1 7
       3 11
       4 10
       5 8
       5 13
       6 10
       7 13
       8 12
       9 11
       11 12
       11 14

       >>> distances = bfs_distances(0)
       >>> print(distances)
       [0, 1, 3, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 3, 2]
    """
    if graph is None:
        N, M = map(int, input().split()) # N - кол-во вершин графа, M - кол-во ребер.
        graph = make_graph(N, M)

    from collections import deque
    distances = [None] * N
    distances[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[cur_v] + 1
                queue.append(neigh_v)

    return distances


def bfs_path(start_vertex, end_vertex, graph=None):
    """Выполняет обход графа graph в ширину.

       Возвращает список вершин, которые посещаются при
       движении по графу от вершины start_vertex к вершине
       end_vertex.

       Тест для графа 15 вершин, 16 ребер:

       0 1
       0 12 
       0 11
       0 10
       2 6
       1 7
       3 11
       4 10
       5 8
       5 13
       6 10
       7 13
       8 12
       9 11
       11 12
       11 14


       >>> path = bfs_path(0, 2)
       >>> print(path)
       [0, 10, 6, 2]
    """

    if graph is None:
        N, M = map(int, input().split())
        graph = make_graph(N, M)
        
    from collections import deque
    parents = [None] * N
    parents[start_vertex] = -1
    queue = deque([start_vertex])
    

    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if parents[neigh_v] is None:
                parents[neigh_v] = cur_v
                queue.append(neigh_v)

    path = [end_vertex]
    parent = parents[end_vertex]
    while parent != - 1:
        path.append(parent)
        parent = parents[parent]

    return path[::-1]
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
