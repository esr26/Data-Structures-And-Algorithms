graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = set()
stack = ["A"]

while stack:
    node = stack.pop()

    if node in visited:
        continue

    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            stack.append(neighbor)

            