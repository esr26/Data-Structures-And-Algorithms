# Agent D — Visual prompts

Created 83 infographic prompts, one for each distinct algorithm or instructional pattern identified across the Python solutions. Every prompt has the requested **When to Use**, **How It Works** (a 4–6 step visual trace with a small example), and **Quick Facts** sections. Prompts are text only; no image generation was performed.

## Grouping decisions

- Combined 3-sum and 4-sum under sorted k-sum, and grouped simple one-pass extrema/count checks under linear scan.
- Shared DFS/BFS across graph traversal, reachable components, flood fill, and unweighted paths, while retaining separate prompts for multi-source BFS, grid region traversal, and shortest-path enumeration.
- Split weighted graph methods when their state or relaxation rule differs: standard Dijkstra, minimax Dijkstra, budgeted-state shortest path, 0-1 BFS, Bellman-Ford, DAG shortest path, and Floyd-Warshall.
- Kept specialized applications separate when the core invariant needs its own explanation, such as car fleets, alien alphabet constraints, and distinct island shapes.
- No prompt was created for topics with no solution implementation, such as tries or tree traversals.

## Prompt files

- `visual_prompts/alien_order_constraints.txt`
- `visual_prompts/answer_search.txt`
- `visual_prompts/bellman_ford.txt`
- `visual_prompts/bidirectional_mapping.txt`
- `visual_prompts/binary_search.txt`
- `visual_prompts/bipartite_coloring.txt`
- `visual_prompts/bounds_search.txt`
- `visual_prompts/boyer_moore.txt`
- `visual_prompts/breadth_first_search.txt`
- `visual_prompts/car_fleet_monotonic.txt`
- `visual_prompts/center_palindrome.txt`
- `visual_prompts/closest_window_binary_search.txt`
- `visual_prompts/collision_stack.txt`
- `visual_prompts/container_water.txt`
- `visual_prompts/continuous_answer_search.txt`
- `visual_prompts/cyclic_placement.txt`
- `visual_prompts/dag_longest_path_dp.txt`
- `visual_prompts/dag_shortest_path.txt`
- `visual_prompts/depth_first_search.txt`
- `visual_prompts/dfs_cycle_toposort.txt`
- `visual_prompts/digit_processing.txt`
- `visual_prompts/dijkstra.txt`
- `visual_prompts/disjoint_set_union.txt`
- `visual_prompts/dutch_flag.txt`
- `visual_prompts/euclidean_gcd.txt`
- `visual_prompts/fixed_sliding_window.txt`
- `visual_prompts/floyd_warshall.txt`
- `visual_prompts/frequency_stack.txt`
- `visual_prompts/frequency_window.txt`
- `visual_prompts/greedy_pairing.txt`
- `visual_prompts/grid_graph_search.txt`
- `visual_prompts/hash_frequency.txt`
- `visual_prompts/histogram_stack.txt`
- `visual_prompts/interval_merge.txt`
- `visual_prompts/island_shape_canonicalization.txt`
- `visual_prompts/k_sum.txt`
- `visual_prompts/kadane.txt`
- `visual_prompts/kahn_topological_sort.txt`
- `visual_prompts/linear_scan.txt`
- `visual_prompts/longest_consecutive_set.txt`
- `visual_prompts/matrix_in_place.txt`
- `visual_prompts/matrix_staircase.txt`
- `visual_prompts/matrix_traversal.txt`
- `visual_prompts/max_product_dp.txt`
- `visual_prompts/merge_count.txt`
- `visual_prompts/merge_sort.txt`
- `visual_prompts/min_stack.txt`
- `visual_prompts/minimax_dijkstra.txt`
- `visual_prompts/minimum_cover_window.txt`
- `visual_prompts/monotonic_deque_window.txt`
- `visual_prompts/monotonic_stack.txt`
- `visual_prompts/multi_source_bfs.txt`
- `visual_prompts/parenthesis_depth.txt`
- `visual_prompts/partition_selection.txt`
- `visual_prompts/pascal_triangle_dp.txt`
- `visual_prompts/peak_search.txt`
- `visual_prompts/prefix_sum_hash.txt`
- `visual_prompts/prefix_xor_hash.txt`
- `visual_prompts/prim_mst.txt`
- `visual_prompts/queue_stack_simulation.txt`
- `visual_prompts/quick_sort.txt`
- `visual_prompts/rainwater.txt`
- `visual_prompts/reversal_rotation.txt`
- `visual_prompts/roman_numeral_scan.txt`
- `visual_prompts/rotated_search.txt`
- `visual_prompts/rotation_by_concatenation.txt`
- `visual_prompts/rpn_stack.txt`
- `visual_prompts/running_min_stock.txt`
- `visual_prompts/shortest_path_parent_dag.txt`
- `visual_prompts/sorted_merge.txt`
- `visual_prompts/sqrt_divisors.txt`
- `visual_prompts/sqrt_prime_test.txt`
- `visual_prompts/stack_parsing.txt`
- `visual_prompts/state_augmented_shortest_path.txt`
- `visual_prompts/string_parser.txt`
- `visual_prompts/substring_enumeration.txt`
- `visual_prompts/tarjan_bridges.txt`
- `visual_prompts/time_map_search.txt`
- `visual_prompts/two_pointer_compaction.txt`
- `visual_prompts/two_pointer_opposite.txt`
- `visual_prompts/unique_substring_window.txt`
- `visual_prompts/variable_sliding_window.txt`
- `visual_prompts/zero_one_bfs.txt`

## Verification

Confirmed 83 text files exist; each includes all three section headings and 4–6 numbered steps. Every cited source file in the prompts exists in the repo.

## Subsequent addition

The root agent later changed `Array & Hashing/find duplicate number.py` to Floyd cycle detection and added `visual_prompts/floyd_cycle_detection.txt`. New graph solutions added `visual_prompts/maximum_probability_path.txt`, `visual_prompts/alternating_color_bfs.txt`, and `visual_prompts/obstacle_budget_bfs.txt`. The current prompt total is 87.
