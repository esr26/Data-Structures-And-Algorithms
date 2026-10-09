class Solution:
    def shortestPath(self,n, m, edges):

        graph = defaultdict(list)
        dist = [float('inf')] * (n + 1)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            

        heap = [(0, 1)]
        dist[1] = 0
        parent = list(range(n+1))

        

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue
            
            for nei, w in graph[node]:
                new_dist = d + w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    parent[nei] = node
                    heapq.heappush(heap, (new_dist, nei))
        
        if dist[n] == float('inf'):
            return [-1]

        path = []
        node = n

        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)
        path.reverse() 
        
        return [dist[n]] + path
            

            