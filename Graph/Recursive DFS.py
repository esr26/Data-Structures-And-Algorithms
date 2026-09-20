graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = set()

def dfs(node):
    visited.add(node)

    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)


dfs("A")
