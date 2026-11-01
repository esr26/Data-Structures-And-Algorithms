from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(
        self,
        n: int,
        redEdges: list[list[int]],
        blueEdges: list[list[int]],
    ) -> list[int]:
        graph = defaultdict(list)

        for u, v in redEdges:
            graph[u].append((v, "red"))
        for u, v in blueEdges:
            graph[u].append((v, "blue"))

        queue = deque([(0, "red", 0), (0, "blue", 0)])
        visited = {(0, "red"), (0, "blue")}
        answer = [-1] * n
        answer[0] = 0

        while queue:
            node, last_color, steps = queue.popleft()

            for neighbor, current_color in graph[node]:
                state = (neighbor, current_color)
                if current_color == last_color or state in visited:
                    continue

                visited.add(state)
                next_steps = steps + 1
                if answer[neighbor] == -1:
                    answer[neighbor] = next_steps
                queue.append((neighbor, current_color, next_steps))

        return answer
