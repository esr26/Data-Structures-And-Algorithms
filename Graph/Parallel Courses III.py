from collections import defaultdict, deque


class Solution:
    def minimumTime(
        self,
        n: int,
        relations: list[list[int]],
        time: list[int],
    ) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()
        finish = [0] * (n + 1)

        for node in range(1, n + 1):
            if indegree[node] == 0:
                queue.append(node)
                finish[node] = time[node - 1]

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                finish[nei] = max(
                    finish[nei],
                    finish[node] + time[nei - 1],
                )

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return max(finish)
