from collections import deque

def shortestPath(n, edges):

    # Build graph
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v, weight in edges:
        graph[u].append((v, weight))
        indegree[v] += 1

    # Topological sort using Kahn's algorithm
    queue = deque()

    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)

    topo = []

    while queue:
        node = queue.popleft()
        topo.append(node)

        for nei, weight in graph[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

    # Shortest distances from source 0
    INF = float("inf")
    dist = [INF] * n
    dist[0] = 0

    # Process in topological order
    for u in topo:

        # Unreachable node
        if dist[u] == INF:
            continue

        for v, weight in graph[u]:

            # Relaxation
            dist[v] = min(
                dist[v],
                dist[u] + weight
            )

    # Convert unreachable nodes to -1
    return [
        -1 if d == INF else d
        for d in dist
    ]

    