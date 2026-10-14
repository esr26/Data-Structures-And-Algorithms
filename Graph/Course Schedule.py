from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def dfs(node):
            state[node] = 1

            for nei in graph[node]:
                if state[nei] == 1:
                    return True

                if state[nei] == 0:
                    if dfs(nei):
                        return True

            state[node] = 2
            return False

        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[v].append(u)

        state = {node: 0 for node in range(numCourses)}

        for node in range(numCourses):
            if dfs(node):
                return False

        return True
