from collections import defaultdict

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:

        n = len(graph)
        color = [-1] * n

        def dfs(node):
            for nei in graph[node]:

                # Neighbor hasn't been colored
                if color[nei] == -1:
                    color[nei] = 1 - color[node]

                    if not dfs(nei):
                        return False

                # Neighbor has the same color
                elif color[nei] == color[node]:
                    return False

            return True

        for node in range(n):

            # Handle disconnected components
            if color[node] == -1:
                color[node] = 0

                if not dfs(node):
                    return False

        return True

        