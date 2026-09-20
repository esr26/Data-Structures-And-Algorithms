from collections import deque

visited = set()
queue = deque(["A"])

while queue:
    node = queue.popleft()

    if node in visited:
        continue

    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            queue.append(neighbor)