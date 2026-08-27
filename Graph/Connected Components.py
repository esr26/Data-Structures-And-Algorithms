from collections import defaultdict

def count_components(V, edges):

    graph = defaultdict(list)

    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    visited = [False] * V
    count = 0

    def dfs(node):
        if visited[node]:
            return

        visited[node] = True

        for neigh in graph[node]:
            dfs(neigh)

    for v in range(V):
        if not visited[v]:
            count += 1
            dfs(v)

    return count

    