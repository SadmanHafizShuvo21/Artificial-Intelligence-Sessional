def dfs(graph, start, vis = False):
    if vis is False:
        vis = set()
    
    print(start, end=" ")     # Visit the node
    vis.add(start)

    for child in graph[start]:
        if child not in vis:
            dfs(graph, child, vis)
# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal:")
dfs(graph, 'A')
