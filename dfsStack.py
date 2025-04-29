def dfs_stack(graph, start):
    visisted = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visisted:
            print(node)
            visisted.add(node)
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}
dfs_stack(graph, 'A')