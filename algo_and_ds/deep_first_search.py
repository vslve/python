def dfs(vertex, graph, visited:set):
    """Осуществляет поиск в глубину по графу graph начиная с вершины vertex.

       graph - словарь вида {вершина: {соседи} - множество}
    """

    visited.add(vertex)


    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour, graph, visited)

def сount_connected_component(graph:dict):
    """Осуществляет подсчет компенент связности графа"""
    
    visited = set()
    count = 0

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, graph, visited)
            count += 1
        
    return count
    
    

       
