from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:

        # All characters that exist in the input
        chars = set("".join(words))

        # Directed graph
        graph = defaultdict(set)

        # Build graph from adjacent words
        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]

            m = min(len(prev), len(curr))

            # Prefix invalid case: ["abc", "ab"]
            if len(prev) > len(curr) and prev[:m] == curr[:m]:
                return ""

            for j in range(m):
                if prev[j] != curr[j]:
                    graph[prev[j]].add(curr[j])
                    break

        # Calculate indegree
        indegree = {char: 0 for char in chars}

        for node in graph:
            for nei in graph[node]:
                indegree[nei] += 1

        # Start with characters having no prerequisites
        queue = deque(
            char for char in chars
            if indegree[char] == 0
        )

        result = []

        # Kahn's algorithm
        while queue:
            node = queue.popleft()
            result.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        # Cycle detection
        if len(result) != len(chars):
            return ""

        return "".join(result)


        