from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        state = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(node):

            # Completely processed → no cycle
            if state[node] == 2:
                return False

            # Currently being explored → cycle
            if state[node] == 1:
                return True

            state[node] = 1

            for nei in graph[node]:
                if dfs(nei):
                    return True

            # Finished exploring this node
            state[node] = 2

            return False

        for node in range(numCourses):
            if dfs(node):
                return False

        return True