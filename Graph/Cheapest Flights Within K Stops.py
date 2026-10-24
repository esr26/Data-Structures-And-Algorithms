from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: list[list[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        dist = [
            [float("inf")] * (k + 2)
            for _ in range(n)
        ]

        dist[src][0] = 0
        min_heap = [(0, src, 0)]

        while min_heap:
            cost, city, flights_used = heapq.heappop(min_heap)

            if cost > dist[city][flights_used]:
                continue

            if flights_used == k + 1:
                continue

            for nei, price in graph[city]:
                new_cost = cost + price
                new_flights = flights_used + 1

                if new_cost < dist[nei][new_flights]:
                    dist[nei][new_flights] = new_cost
                    heapq.heappush(
                        min_heap,
                        (new_cost, nei, new_flights),
                    )

        answer = min(dist[dst])
        return answer if answer != float("inf") else -1
