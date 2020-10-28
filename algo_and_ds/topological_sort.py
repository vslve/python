def dfs(start, graph, visited, ans):
    """Осущестаялет обход графа graph, не содержащего циклы,
       в глубину, начиная с вершины start(номер вершины).

       visited - список вершин с отметкой о их посещении:
       если visited[номер вершины] == True - вершина посещена,
       если == False - не посещена.

       Наполняет писок ans номерами вершин от большей к меньшей.
    """

    visited[start] = True
    for vertex in graph[visited]:
        if not visited[vertex]:
            dfs(vertex, graph, visited, ans)
            ans.append(vertex) # добавляем номер вершины максимальной глубины
                               # для каждого обхода
    

    



def topological_sorting(graph, n: int):



    visited = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, graph, visited, ans)

    ans[:] = ans[::-1]

    return ans
