from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        def dfs(node):
            while graph[node]:
                neighbor = graph[node].pop()
                dfs(neighbor)
            result.append(node)

        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)

        for destinations in graph.values():
            destinations.sort(reverse=True)

        result = []
        dfs("JFK")
        return result[::-1]
