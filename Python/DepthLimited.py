def dls(graph, st, goal, limit, path = None):
    if path is None:
        path = [] #list

    print("Visiting:", st)
    path.append(st)

    if st == goal:
        return path

    if limit == 0:   # depth limit reached
        path.pop()
        return None

    for child in graph[st]:
        if child not in path:  # avoid cycles
            result = dls(graph, child, goal, limit - 1, path)
            if result:
                return result

    path.pop()
    return None


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Depth Limited Search:")
result = dls(graph, 'A', 'F', 2)   # depth limit = 2
print("Result Path:", result)
