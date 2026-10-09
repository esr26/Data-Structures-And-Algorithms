import heapq
class Solution:
    def dijkstra(self, V, edges, S):

        graph = [[] for _ in range(V)]

        dist = [float('inf')] * V

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        heap = [(0, S)]
        dist[S] = 0

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            
            for nei, w in graph[node]:
                new_dist = d + w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))
            
        return [10**9 if d == float('inf') else d for d in dist]
    

    