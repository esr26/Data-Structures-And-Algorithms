from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        completed = 0
        order = []

        while queue:
            node = queue.popleft()
            completed += 1
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return order if completed == numCourses else []
