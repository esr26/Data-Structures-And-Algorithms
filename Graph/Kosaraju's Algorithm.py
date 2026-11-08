from collections import defaultdict


class Solution:
    def kosaraju(self, V, edges):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)

        visited = set()
        order = []

        def dfs1(node):
            visited.add(node)
            stack = [(node, iter(graph[node]))]

            while stack:
                current, neighbors = stack[-1]
                neighbor = next(neighbors, None)
                if neighbor is None:
                    order.append(current)
                    stack.pop()
                elif neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, iter(graph[neighbor])))

        for node in range(V):
            if node not in visited:
                dfs1(node)

        visited.clear()

        def dfs2(node):
            visited.add(node)
            stack = [node]

            while stack:
                for neighbor in reverse_graph[stack.pop()]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        scc_count = 0
        for node in reversed(order):
            if node not in visited:
                dfs2(node)
                scc_count += 1

        return scc_count
