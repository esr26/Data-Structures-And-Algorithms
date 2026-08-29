class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):

            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            
            state[course] = 1

            for neigh in graph[course]:

                if not dfs(neigh):
                    return False
            
            state[course] = 2
            return True


        
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c2].append(c1)

        state = [0] * numCourses
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True



