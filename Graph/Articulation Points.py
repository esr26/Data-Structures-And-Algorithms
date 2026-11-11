class Solution:
    def articulationPoints(self, n, adj):
        disc = [-1] * n
        low = [-1] * n
        parent = [-1] * n
        children = [0] * n
        articulation_points = set()
        timer = 0

        for root in range(n):
            if disc[root] != -1:
                continue

            disc[root] = low[root] = timer
            timer += 1
            stack = [(root, iter(adj[root]))]

            while stack:
                node, neighbors = stack[-1]
                try:
                    neighbor = next(neighbors)
                except StopIteration:
                    stack.pop()
                    p = parent[node]

                    if p == -1:
                        if children[node] > 1:
                            articulation_points.add(node)
                    else:
                        low[p] = min(low[p], low[node])
                        if parent[p] != -1 and low[node] >= disc[p]:
                            articulation_points.add(p)
                    continue

                if neighbor == parent[node]:
                    continue

                if disc[neighbor] == -1:
                    parent[neighbor] = node
                    children[node] += 1
                    disc[neighbor] = low[neighbor] = timer
                    timer += 1
                    stack.append((neighbor, iter(adj[neighbor])))
                else:
                    low[node] = min(low[node], disc[neighbor])

        return sorted(articulation_points) if articulation_points else [-1]
