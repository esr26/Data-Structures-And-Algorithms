# Graph

Use a graph model when entities connect through edges. Match the algorithm to the question: BFS for unweighted shortest paths, DFS for reachability/components, Dijkstra for nonnegative weighted paths or maximum path probability, topological sort for dependencies, and MST algorithms for minimum connection cost.

## Problem-solving workflow

1. Define vertices, directedness, weights, and whether the input is a grid or explicit edge list.
2. Choose an adjacency representation and the state needed for each visit or path.
3. Choose BFS/DFS, shortest path, topological sort, or MST from the objective and edge weights.
4. Initialize every source or starting state, including its distance/visited value.
5. Process a frontier or sorted edges; relax distances or record visits only when the state improves.
6. Handle unreachable nodes, cycles, and the requested output format.

**Complexity:** BFS/DFS and topological sort are O(V + E) time and O(V + E) storage with adjacency lists. Heap Dijkstra is O((V + E) log V) time and O(V + E) storage; it requires nonnegative weights. Bellman–Ford is O(VE), Floyd–Warshall O(V³), and Kruskal/Prim-style MSTs typically O(E log V) with appropriate data structures. Grid traversals use V = rows × columns; obstacle-budget BFS has O(rows × columns × (k + 1)) states.

**Pitfalls:** Mark visits at the right time; skip stale heap entries; keep extra state when constraints such as stops or edge colors matter. For alternating-color BFS, mark `(node, arrival_color)` and carry each path's depth in its queue entry. For obstacle-elimination BFS, mark `(row, column, remaining_budget)` only after checking the budget, and compute a fresh budget for each neighbor. A path's effort in `Path With Minimum Effort` is the maximum edge difference on that path, so relax with `max(current_effort, edge_difference)`. For `Path With Maximum Probability`, multiply the current probability by the edge probability and relax only when the product improves the best known value. Check whether a cycle, disconnected graph, or unreachable destination changes the requested return value.
