from collections import deque


def zero_one_bfs(graph, n, start):
    dist = [float("inf")] * n
    dist[start] = 0

    queue = deque([start])

    while queue:
        node = queue.popleft()

        for nei, weight in graph[node]:
            new_dist = dist[node] + weight

            if new_dist < dist[nei]:
                dist[nei] = new_dist

                if weight == 0:
                    queue.appendleft(nei)
                else:
                    queue.append(nei)

    return dist
