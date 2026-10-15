from collections import defaultdict


class Solution:
    def criticalConnections(
        self,
        n: int,
        connections: list[list[int]],
    ) -> list[list[int]]:
        def dfs(node, parent):
            nonlocal timer

            disc[node] = low[node] = timer
            timer += 1

            for nei in graph[node]:
                if nei == parent:
                    continue

                if disc[nei] == -1:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])

                    if low[nei] > disc[node]:
                        bridges.append([node, nei])
                else:
                    low[node] = min(low[node], disc[nei])

        disc = [-1] * n
        low = [-1] * n
        graph = defaultdict(list)
        timer = 0
        bridges = []

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            if disc[node] == -1:
                dfs(node, -1)

        return bridges
