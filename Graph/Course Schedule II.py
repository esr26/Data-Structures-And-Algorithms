class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        indegree = [0] * numCourses
        graph = defaultdict(list)

        for c, pre in prerequisites:
            graph[pre].append(c)
            indegree[c] += 1
        
        queue = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        return order if len(order)==numCourses else []

        

        