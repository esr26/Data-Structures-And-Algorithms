# Agent B — Solution quality review

Reviewed **157 Python files** in the 10 topic folders. Complexities describe the implementation as written, using `n` for a one-dimensional input, `m × n` for a grid, `V/E` for graph vertices/edges, `L` for word length, `Σ` for alphabet size, `R/S/M` for a binary-search numeric range, and `α` for inverse Ackermann. Output storage is excluded only where stated. `—` means no concrete issue found under the usual problem constraints; it is not a proof of correctness.

## Confirmed blockers

**Python compilation fails (8 files):**

- `Array & Hashing/count inversion.py` — line 39: 'return' outside function.
- `Array & Hashing/count subarrays with xor equals target.py` — line 14: 'return' outside function.
- `Array & Hashing/count subarrays with xor.py` — line 14: 'return' outside function.
- `Array & Hashing/leaders in the array.py` — line 16: 'return' outside function.
- `Array & Hashing/longest subarray sum equal to 0.py` — line 16: 'return' outside function.
- `Binary Search/floor and ceil in a sorted array.py` — line 12: 'return' outside function.
- `Graph/Minimum moves to each (m,n).py` — line 6: 'return' outside function.
- `Two Pointers/move zeros to end.py` — line 12: 'return' outside function.

**Missing non-typing imports (12 files), causing a runtime `NameError` when the affected code runs:**

- `Binary Search/minimum gas stations.py` — math.
- `Binary Search/time based key value search.py` — defaultdict.
- `Graph/01 Matrix.py` — deque.
- `Graph/Minimum moves to each (m,n).py` — deque.
- `Graph/Print Shortest Path.py` — defaultdict, heapq.
- `Graph/Shortest Path in Binary Matrix.py` — heapq.
- `Graph/Word Ladder II.py` — defaultdict, deque.
- `Sliding Window/permutation string.py` — Counter.
- `Sliding Window/sliding-window-maximum.py` — collections.
- `Stacks/implement-stack-using-queues.py` — deque.
- `Stacks/maximum-frequency-stack.py` — defaultdict.
- `Strings/sort-characters-by-frequency.py` — Counter.

**Unimported `List` annotations (65 files):** these fail at class/function definition when run as standalone Python, although some online judges inject `List`. Exact paths:

- `Array & Hashing/check if array sorted and rotated.py`
- `Array & Hashing/find duplicate number.py`
- `Array & Hashing/first missing positive integer.py`
- `Array & Hashing/longest common prefix.py`
- `Array & Hashing/longest-consecutive-sequence.py`
- `Array & Hashing/majority element 2.py`
- `Array & Hashing/majority element I.py`
- `Array & Hashing/maximum product subarray.py`
- `Array & Hashing/maximum subarray sum (Kadane's Algo).py`
- `Array & Hashing/merge intervals.py`
- `Array & Hashing/missing number.py`
- `Array & Hashing/pascal's triangle.py`
- `Array & Hashing/remove duplicates from array.py`
- `Array & Hashing/remove-element.py`
- `Array & Hashing/reverse pairs.py`
- `Array & Hashing/rotate array.py`
- `Array & Hashing/rotate matrix.py`
- `Array & Hashing/set matrix zeros.py`
- `Array & Hashing/sort colors.py`
- `Array & Hashing/spiral matrix.py`
- `Array & Hashing/subarray sum equals k.py`
- `Binary Search/Find a Peak Element II.py`
- `Binary Search/Find the Smallest Divisor Given a Threshold.py`
- `Binary Search/Minimum Number of Days to Make m Bouquets.py`
- `Binary Search/Search a 2D Matrix II.py`
- `Binary Search/aggressive cows.py`
- `Binary Search/binary search.py`
- `Binary Search/capacity to ship within d days.py`
- `Binary Search/count occurrences of a number in a sorted array.py`
- `Binary Search/find first and last occurence.py`
- `Binary Search/find peak element.py`
- `Binary Search/find-minimum-in-rotated-sorted-array.py`
- `Binary Search/koko eating bananas.py`
- `Binary Search/kth missing positive integer.py`
- `Binary Search/median of two sorted arrays.py`
- `Binary Search/minimum gas stations.py`
- `Binary Search/search in 2d matrix.py`
- `Binary Search/search in rotated sorted array ii.py`
- `Binary Search/search-in-rotated-sorted-array.py`
- `Binary Search/search-insert-position.py`
- `Binary Search/split-array-largest-sum.py`
- `Bit Manupulation/Single Number.py`
- `Graph/Number of Islands.py`
- `Graph/number of provinces.py`
- `Sliding Window/best-time-to-buy-and-sell-stock.py`
- `Sliding Window/contains duplicate ii.py`
- `Sliding Window/find-k-closest-elements.py`
- `Sliding Window/minimum length subarray sum.py`
- `Sliding Window/sliding-window-maximum.py`
- `Stacks/asteroid collision.py`
- `Stacks/baseball-game.py`
- `Stacks/car-fleet.py`
- `Stacks/daily temperatures.py`
- `Stacks/evaluate-reverse-polish-notation.py`
- `Stacks/largest rectangle histogram.py`
- `Stacks/majority element 2.py`
- `Two Pointers/4_sum.py`
- `Two Pointers/boats to save people.py`
- `Two Pointers/container with most water.py`
- `Two Pointers/maximum consecutive ones.py`
- `Two Pointers/merge_two_sorted arrays.py`
- `Two Pointers/move zeros to end.py`
- `Two Pointers/rotate array.py`
- `Two Pointers/trapping rain water.py`
- `Two Pointers/two_sum_ii_sorted_array.py`

**Other confirmed standalone failure:** `Graph/Iterative BFS.py` references `graph` without defining it. `Array & Hashing/find duplicate number.py` mutates its input, contrary to the no-modification constraint of LeetCode 287.

## Per-file findings

### Array & Hashing

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Array & Hashing/check if array is sorted.py` | Single pass adjacent comparison | O(n) | O(1) | — |
| `Array & Hashing/check if array sorted and rotated.py` | Count circular descents | O(n) | O(1) | Unimported `List` |
| `Array & Hashing/count inversion.py` | Merge-sort inversion counting | O(n log n) | O(n) | Bare top-level return and undefined arr; Does not compile |
| `Array & Hashing/count subarrays with xor equals target.py` | Prefix XOR frequency map | O(n) | O(n) | Bare top-level return; nums and k undefined; Does not compile |
| `Array & Hashing/count subarrays with xor.py` | Prefix XOR frequency map | O(n) | O(n) | Bare top-level return; nums and k undefined; duplicate of prior file; Does not compile |
| `Array & Hashing/find duplicate number.py` | Cyclic placement | O(n) | O(1) | Mutates nums, violating LeetCode 287's no-modification requirement; Unimported `List` |
| `Array & Hashing/find repeating and missing numbers.py` | Sum and squared-sum equations | O(n) | O(1) | Assumes exactly one repeat and one missing; otherwise division by zero possible |
| `Array & Hashing/find second largest and smallest.py` | Extrema scan | O(n) | O(1) | Returns -1 unless both distinct second extrema exist |
| `Array & Hashing/first missing positive integer.py` | Cyclic placement | O(n) | O(1) | Mutates input, as intended by problem; Unimported `List` |
| `Array & Hashing/leaders in the array.py` | Reverse scan with running maximum | O(n) | O(n) | Bare top-level return; nums undefined; Does not compile |
| `Array & Hashing/longest common prefix.py` | Vertical character scan | O(total compared characters) | O(1) extra | Empty strs raises IndexError; Unimported `List` |
| `Array & Hashing/longest subarray sum equal to 0.py` | Earliest prefix-sum index | O(n) | O(n) | Bare top-level return; nums undefined; Does not compile |
| `Array & Hashing/longest subarray sums equal to K.py` | Earliest prefix-sum index | O(n) | O(n) | — |
| `Array & Hashing/longest-consecutive-sequence.py` | Hash-set sequence starts | O(n) expected | O(n) | Unimported `List` |
| `Array & Hashing/majority element 2.py` | Boyer-Moore, two candidates | O(n) | O(1) | Unimported `List` |
| `Array & Hashing/majority element I.py` | Boyer-Moore majority vote | O(n) | O(1) | Relies on a guaranteed majority; empty nums leaves ele undefined; Unimported `List` |
| `Array & Hashing/maximum product subarray.py` | Bidirectional prefix/suffix products | O(n) | O(1) | Unimported `List` |
| `Array & Hashing/maximum subarray sum (Kadane's Algo).py` | Kadane running sum | O(n) | O(1) | Unimported `List` |
| `Array & Hashing/merge intervals.py` | Sort then merge overlaps | O(n log n) | O(n) output | Mutates input intervals and the nested interval lists; Unimported `List` |
| `Array & Hashing/missing number.py` | Cyclic placement | O(n) | O(1) | Mutates nums; Unimported `List` |
| `Array & Hashing/pascal's triangle.py` | Row-by-row dynamic construction | O(r²) | O(r²) output | Unimported `List` |
| `Array & Hashing/remove duplicates from array.py` | Slow/fast pointers | O(n) | O(1) | Empty nums returns 1 instead of 0; Unimported `List` |
| `Array & Hashing/remove-element.py` | Two-ended in-place partition | O(n) | O(1) | Changes element order; acceptable for LeetCode 27; Unimported `List` |
| `Array & Hashing/reverse pairs.py` | Merge-sort cross-pair counting | O(n log n) | O(n) | Unimported `List` |
| `Array & Hashing/rotate array.py` | Three in-place reversals | O(n) | O(1) | Empty nums causes division by zero; Unimported `List` |
| `Array & Hashing/rotate matrix.py` | Transpose then reverse rows | O(n²) | O(1) | Unimported `List` |
| `Array & Hashing/set matrix zeros.py` | Record zero rows and columns | O(mn) | O(m+n) | Requires nonempty matrix; returns matrix despite None annotation; Unimported `List` |
| `Array & Hashing/sort colors.py` | Dutch national flag | O(n) | O(1) | Returns nums despite None annotation; Unimported `List` |
| `Array & Hashing/spiral matrix.py` | Shrinking boundary traversal | O(mn) | O(1) extra | Empty matrix raises IndexError; Unimported `List` |
| `Array & Hashing/subarray sum equals k.py` | Prefix-sum frequency map | O(n) | O(n) | Unimported `List` |

### Binary Search

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Binary Search/aggressive cows.py` | Sort and binary search feasible spacing | O(n log n + n log R) | O(1) extra | No explicit infeasible-k check; Unimported `List` |
| `Binary Search/Allocate Minimum Number of Pages.py` | Binary search maximum pages | O(n log S) | O(1) | Empty arr raises ValueError at max |
| `Binary Search/binary search.py` | Iterative binary search | O(log n) | O(1) | Unimported `List` |
| `Binary Search/capacity to ship within d days.py` | Binary search capacity | O(n log S) | O(1) | Empty weights raises ValueError; Unimported `List` |
| `Binary Search/count occurrences of a number in a sorted array.py` | First/last-bound binary searches | O(log n) | O(1) | Unimported `List` |
| `Binary Search/Find a Peak Element II.py` | Binary search columns, scan column max | O(m log n) | O(1) | Empty matrix raises IndexError; Unimported `List` |
| `Binary Search/find first and last occurence.py` | First/last-bound binary searches | O(log n) | O(1) | Unimported `List` |
| `Binary Search/Find out how many times the array has been rotated.py` | Binary search rotation minimum index | O(log n) | O(1) | Duplicates can break strict logarithmic/correct rotation interpretation |
| `Binary Search/find peak element.py` | Binary search rising slope | O(log n) | O(1) | Unimported `List` |
| `Binary Search/Find the Smallest Divisor Given a Threshold.py` | Binary search feasible divisor | O(n log M) | O(1) | Assumes feasible threshold at least n; Unimported `List` |
| `Binary Search/find-minimum-in-rotated-sorted-array.py` | Binary search minimum | O(log n) | O(1) | Assumes distinct values and nonempty nums; Unimported `List` |
| `Binary Search/floor and ceil in a sorted array.py` | Binary search neighboring bounds | O(log n) | O(1) | Bare top-level returns; nums and target undefined; Does not compile |
| `Binary Search/guess the number.py` | Binary search through guess API | O(log n) | O(1) | Requires external guess API |
| `Binary Search/K-th Element of two sorted arrays.py` | Binary search partition | O(log min(m,n)) | O(1) | Invalid k can yield infinity or -1; expects 1-based valid k |
| `Binary Search/koko eating bananas.py` | Binary search eating speed | O(n log M) | O(1) | Unused ans variable; assumes feasible h at least pile count; Unimported `List` |
| `Binary Search/kth missing positive integer.py` | Binary search missing-count threshold | O(log n) | O(1) | Unimported `List` |
| `Binary Search/median of two sorted arrays.py` | Binary search balanced partition | O(log min(m,n)) | O(1) | Both arrays empty has no defined median; Unimported `List` |
| `Binary Search/minimum gas stations.py` | Binary search floating maximum gap | O(n log(R/ε)) | O(1) | math not imported; fewer than 2 stations fails; Unimported `List`, `math` |
| `Binary Search/Minimum Number of Days to Make m Bouquets.py` | Binary search feasible day | O(n log R) | O(1) | Empty bloomDay raises ValueError when m=0; Unimported `List` |
| `Binary Search/nth root of a number.py` | Binary search integer root | O(n log m) arithmetic | O(1) | Assumes positive n and m |
| `Binary Search/Search a 2D Matrix II.py` | Top-right staircase search | O(m+n) | O(1) | Empty matrix raises IndexError; Unimported `List` |
| `Binary Search/search in 2d matrix.py` | Binary search flattened matrix | O(log(mn)) | O(1) | Empty matrix raises IndexError; Unimported `List` |
| `Binary Search/search in rotated sorted array ii.py` | Binary search with duplicate contraction | O(n) worst | O(1) | Unimported `List` |
| `Binary Search/search-in-rotated-sorted-array.py` | Binary search sorted half | O(log n) | O(1) | Assumes distinct values; Unimported `List` |
| `Binary Search/search-insert-position.py` | Binary search lower bound | O(log n) | O(1) | Unimported `List` |
| `Binary Search/split-array-largest-sum.py` | Binary search maximum subarray sum | O(n log S) | O(1) | Assumes nonempty nums and nonnegative values; Unimported `List` |
| `Binary Search/sqrt(x).py` | Binary search integer square root | O(log x) | O(1) | — |
| `Binary Search/time based key value search.py` | Append per key, binary search timestamp | set O(1), get O(log q) | O(total sets) | defaultdict not imported; assumes timestamps append in order; Unimported `defaultdict` |

### Bit Manupulation

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Bit Manupulation/Single Number.py` | XOR cancellation | O(n) | O(1) | Unimported `List` |

### Graph

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Graph/0-1 BFS.py` | Deque-based 0/1 shortest paths | O(V+E) | O(V) | Assumes every edge weight is 0 or 1 |
| `Graph/01 Matrix.py` | Multi-source BFS from zeros | O(mn) | O(mn) | deque not imported; mutates mat; Unimported `deque` |
| `Graph/Alien Dictionary.py` | Build precedence graph, Kahn topological sort | O(L+C+E) | O(C+E) | Order among unconstrained characters is nondeterministic but valid |
| `Graph/Bellman-Ford Algorithm.py` | Repeated edge relaxation and cycle check | O(VE) | O(V) | Returns -1 for reachable negative cycle; callers must handle mixed return type |
| `Graph/Bipartite BFS.py` | BFS two-coloring | O(V+E) | O(V) | — |
| `Graph/Bipartite DFS.py` | Recursive DFS two-coloring | O(V+E) | O(V) | Deep graphs may exceed Python recursion limit |
| `Graph/Cheapest Flights Within K Stops.py` | Dijkstra over city and flight-count states | O(kE log(kE)) | O(kV+kE) | — |
| `Graph/Connected Components.py` | Recursive DFS over undirected graph | O(V+E) | O(V+E) | Deep graph may exceed recursion limit |
| `Graph/Connecting Cities With Minimum Cost.py` | Lazy Prim minimum spanning tree | O(E log E) | O(V+E) | Assumes 1-based city labels |
| `Graph/Course Schedule II.py` | Kahn topological sort | O(V+E) | O(V+E) | — |
| `Graph/Course Schedule.py` | DFS cycle detection with three states | O(V+E) | O(V+E) | Rechecks completed nodes in outer loop; deep graph may exceed recursion limit |
| `Graph/Critical Connections in a Network.py` | Tarjan bridge low-link DFS | O(V+E) | O(V+E) | Deep graph may exceed recursion limit; parent-node skip assumes no parallel edges |
| `Graph/Dijikstra Algorithm.py` | Heap Dijkstra on undirected graph | O(E log E) | O(V+E) | Assumes nonnegative weights and undirected edges |
| `Graph/Find Eventual Safe States.py` | DFS cycle reachability with states | O(V+E) | O(V+E) | Deep graph may exceed recursion limit |
| `Graph/Find the City With the Smallest Number of Neighbors at a Threshold Distance.py` | Floyd-Warshall all-pairs shortest paths | O(V³) | O(V²) | — |
| `Graph/Flood fill.py` | Queue BFS recoloring | O(mn) | O(mn) | Mutates image; assumes valid start coordinate |
| `Graph/Floyd-Warshall Algorithm.py` | All-pairs relaxation and negative-cycle check | O(V³) | O(V²) | Directed graph assumed; negative-cycle distances are not meaningful |
| `Graph/Iterative BFS.py` | Queue graph traversal | O(V+E) reachable | O(V) | graph is undefined; script fails at runtime |
| `Graph/Iterative DFS.py` | Stack graph traversal | O(V+E) reachable | O(V) | Fixed demo graph; prints on import |
| `Graph/Min Cost to Connect All Points.py` | Kruskal with union-find over all Manhattan edges | O(n² log n) | O(n²) | Quadratic edge storage may be costly for large n |
| `Graph/Minimum Cost to Make at Least One Valid Path in a Grid.py` | 0-1 BFS on grid directions | O(mn) typical | O(mn) | — |
| `Graph/Minimum moves to each (m,n).py` | BFS on unblocked grid cells | O(mn) | O(mn) | Bare top-level returns; grid undefined and deque not imported; Does not compile; Unimported `deque` |
| `Graph/Multi-Source BFS Shortest Distance.py` | Multi-source BFS to target | O(mn) | O(mn) | Traverses every cell regardless of its symbol; obstacle semantics NEEDS REVIEW |
| `Graph/Network Delay Time.py` | Heap Dijkstra from source | O(E log E) | O(V+E) | Assumes positive/nonnegative edge weights |
| `Graph/Number of distinct islands.py` | DFS movement-path shape encoding | O(mn) | O(mn) | Recursive DFS may exceed stack limit |
| `Graph/number of enclaves.py` | Boundary flood-fill DFS | O(mn) | O(mn) | Mutates grid; deep landmass may exceed recursion limit |
| `Graph/Number of Islands.py` | Recursive flood-fill DFS | O(mn) | O(mn) | Mutates grid; deep island may exceed recursion limit; Unimported `List` |
| `Graph/number of provinces.py` | DFS over adjacency matrix | O(n²) | O(n) | Deep DFS may exceed recursion limit; Unimported `List` |
| `Graph/Parallel Courses III.py` | Topological longest-path dynamic programming | O(V+E) | O(V+E) | No cycle detection; relies on DAG guarantee |
| `Graph/Parallel Courses.py` | Layered Kahn topological sort | O(V+E) | O(V+E) | — |
| `Graph/Path With Minimum Effort.py` | Minimax Dijkstra on grid | O(mn log(mn)) | O(mn) | — |
| `Graph/Prim's Algorithm.py` | Lazy Prim minimum spanning tree | O(E log E) | O(V+E) | Assumes 0-based vertex labels |
| `Graph/Print Shortest Path.py` | Dijkstra with parent reconstruction | O(E log E) | O(V+E) | defaultdict and heapq not imported; Unimported `defaultdict`, `heapq` |
| `Graph/Recursive DFS.py` | Recursive graph traversal | O(V+E) reachable | O(V) | Fixed demo graph; prints on import; deep graph may exceed recursion limit |
| `Graph/Redundant Connection.py` | Union-find cycle detection | O(E α(V)) | O(V) | Array size assumes node labels at most edge count |
| `Graph/Rotting Oranges.py` | Multi-source layered BFS | O(mn) | O(mn) | Mutates grid |
| `Graph/Shorted Path in DAG.py` | Topological order then edge relaxation | O(V+E) | O(V+E) | Does not signal cycles; assumes a DAG and source 0 |
| `Graph/Shortest Path in Binary Matrix.py` | Heap shortest path on 8-neighbor grid | O(mn log(mn)) | O(mn) | heapq not imported; BFS would avoid heap; Unimported `heapq` |
| `Graph/Shortest path in undirected graph with unit weights.py` | BFS from vertex 0 | O(V+E) | O(V+E) | M parameter unused; assumes source 0 |
| `Graph/Surrounded regions.py` | Boundary flood-fill DFS | O(mn) | O(mn) | Mutates board; large region may exceed recursion limit |
| `Graph/Word Ladder I.py` | BFS over one-letter word mutations | O(26 N L²) | O(NL) | — |
| `Graph/Word Ladder II.py` | Level BFS plus predecessor DAG and DFS backtracking | O(26 N L² + output size) | O(NL + output size) | deque and defaultdict not imported; Unimported `defaultdict`, `deque` |

### Math

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Math/check if armstrong number.py` | Digit count and power sum | O(d) | O(1) | Negative n causes nonterminating floor-division loop; nonnegative domain required |
| `Math/check prime number.py` | Trial division through square root | O(√n) | O(1) | Returns strings rather than boolean |
| `Math/gcd of two numbers.py` | Euclidean algorithm | O(log min(a,b)) | O(1) | — |
| `Math/palindrome.py` | Reverse half the digits | O(d) | O(1) | — |
| `Math/print all divisors of a number.py` | Square-root divisor pairs then sort | O(√n log n) worst | O(√n) | Assumes positive n |
| `Math/reverse integer.py` | Digit extraction with signed overflow check | O(d) | O(1) | — |

### Sliding Window

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Sliding Window/best-time-to-buy-and-sell-stock.py` | Running minimum price | O(n) | O(1) | Empty prices raises IndexError; Unimported `List` |
| `Sliding Window/contains duplicate ii.py` | Last-seen index map | O(n) | O(n) | Unimported `List` |
| `Sliding Window/find-k-closest-elements.py` | Shrink sorted window from farther end | O(n-k) | O(1) extra | Assumes sorted arr and valid k; Unimported `List` |
| `Sliding Window/longest-repeating-character-replacement.py` | Frequency sliding window | O(n) | O(Σ) | — |
| `Sliding Window/longest-substring-without-repeating-characters.py` | Unique-character sliding window | O(n) | O(Σ) | — |
| `Sliding Window/minimum length subarray sum.py` | Positive-sum sliding window | O(n) | O(1) | Requires positive numbers; negative values break shrinking rule; Unimported `List` |
| `Sliding Window/minimum-window-substring.py` | Required-count sliding window | O(n+len(t)) | O(Σ) | Empty t causes left index to run past s |
| `Sliding Window/permutation string.py` | Fixed-size frequency window | O(n+len(s1)) | O(Σ) | Counter not imported; equal-dictionary comparison cost depends on alphabet size; Unimported `Counter` |
| `Sliding Window/sliding-window-maximum.py` | Monotonic deque of indices | O(n) | O(k) | collections not imported; Unimported `List`, `collections` |

### Sorting

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Sorting/merge sort.py` | Recursive merge sort | O(n log n) | O(n) | Demo prints on import |
| `Sorting/quick sort.py` | Lomuto quicksort, last-element pivot | O(n log n) average; O(n²) worst | O(log n) average; O(n) worst recursion | Sorted/equal inputs trigger quadratic time and deep recursion; demo prints on import |

### Stacks

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Stacks/asteroid collision.py` | Collision simulation stack | O(n) | O(n) | Unimported `List` |
| `Stacks/baseball-game.py` | Stack of scores | O(n) | O(n) | Assumes valid operation history; + with one score fails; Unimported `List` |
| `Stacks/car-fleet.py` | Sort by position, stack arrival times | O(n log n) | O(n) | Unimported `List` |
| `Stacks/daily temperatures.py` | Monotonic decreasing stack | O(n) | O(n) | Unimported `List` |
| `Stacks/decoded string.py` | Bracket stack decoding | O(output length²) worst due front prepends | O(output length) | Repeated string prepending makes long decoded segments costly |
| `Stacks/evaluate-reverse-polish-notation.py` | Operand stack | O(n) | O(n) | int(val2/val1) converts to float; large integers can lose precision or overflow; Unimported `List` |
| `Stacks/implement-queue-using-stacks.py` | Two-stack queue with full reversal on pop | push O(1), pop O(n), peek O(1) | O(n) | Correct FIFO, but pop copies/reverses and is not amortized O(1) |
| `Stacks/implement-stack-using-queues.py` | Two-queue stack rotation | push O(1), pop/top O(n) | O(n) | deque not imported; Unimported `deque` |
| `Stacks/largest rectangle histogram.py` | Monotonic increasing stack | O(n) | O(n) | Unimported `List` |
| `Stacks/majority element 2.py` | Boyer-Moore, two candidates | O(n) | O(1) | Duplicate of Array & Hashing variant; Unimported `List` |
| `Stacks/maximum-frequency-stack.py` | Frequency map and per-frequency stacks | push/pop O(1) average | O(n) | defaultdict not imported; Unimported `defaultdict` |
| `Stacks/min-stack.py` | Paired value and minimum stacks | push/pop/top/min O(1) | O(n) | — |
| `Stacks/online-stock-span.py` | Monotonic span stack | O(1) amortized per next | O(n) | — |
| `Stacks/simplify-path.py` | Component stack | O(n) | O(n) | — |
| `Stacks/valid-parentheses.py` | Delimiter stack | O(n) | O(n) | Any unexpected non-opening char treated as closing delimiter |

### Strings

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Strings/Count Number of Substrings.py` | At-most-k distinct counts difference | O(n) | O(Σ) | k=0 triggers atMost(-1) and out-of-bounds access |
| `Strings/isomorphic-strings.py` | Two-way character maps | O(n) | O(Σ) | — |
| `Strings/largest-odd-number-in-string.py` | Reverse scan for odd final digit | O(n) | O(1) extra | — |
| `Strings/longest-palindromic-substring.py` | Expand around each center | O(n²) | O(1) extra | — |
| `Strings/maximum-nesting-depth-of-the-parentheses.py` | Parenthesis depth counter | O(n) | O(1) | Assumes valid parentheses; negative depth otherwise |
| `Strings/remove-outermost-parentheses.py` | Depth counter, omit boundary parentheses | O(n) | O(n) | Assumes valid primitive decomposition |
| `Strings/reverse words in a string.py` | Split, reverse, join words | O(n) | O(n) | — |
| `Strings/roman to integer.py` | Subtractive-pair scan | O(n) | O(1) | Assumes valid Roman numerals |
| `Strings/rotate string.py` | Substring search in doubled string | O(n) average | O(n) | Search complexity depends on Python substring implementation |
| `Strings/sort-characters-by-frequency.py` | Frequency buckets | O(n+Σ) | O(n+Σ) | Counter not imported; Unimported `Counter` |
| `Strings/String to Integer (atoi).py` | Trim, sign and digit parsing | O(n) | O(n) due strip | isdigit accepts non-ASCII digits but ord subtraction assumes ASCII |
| `Strings/sum of beauty of all subtrings.py` | Enumerate substrings with incremental counts | O(n²Σ) | O(Σ) | max/min scan each substring; Σ=26 under lowercase constraint |
| `Strings/Valid Anagram.py` | Fixed 26-letter frequency array | O(n) | O(1) | Assumes lowercase ASCII letters only |

### Two Pointers

| File | Algorithm / pattern | Time | Space | Findings |
| --- | --- | --- | --- | --- |
| `Two Pointers/3_sum.py` | Sort, fixed first value and two pointers | O(n²) | O(1) extra excluding output/sort stack | Duplicate unreachable return; mutates nums by sorting |
| `Two Pointers/4_sum.py` | Sort, two fixed values and two pointers | O(n³) | O(1) extra excluding output/sort stack | Mutates nums by sorting; Unimported `List` |
| `Two Pointers/boats to save people.py` | Sort and pair lightest with heaviest | O(n log n) | O(1) extra | Mutates people by sorting; Unimported `List` |
| `Two Pointers/container with most water.py` | Converging pointers toward taller line | O(n) | O(1) | Unimported `List` |
| `Two Pointers/maximum consecutive ones.py` | Running streak | O(n) | O(1) | Unimported `List` |
| `Two Pointers/merge_two_sorted arrays.py` | Backward in-place merge | O(m+n) | O(1) | Returns nums1 despite None annotation; Unimported `List` |
| `Two Pointers/move zeros to end.py` | Slow/fast in-place partition | O(n) | O(1) | Return is outside function; file fails compilation; Does not compile; Unimported `List` |
| `Two Pointers/rotate array.py` | Three in-place reversals | O(n) | O(1) | Empty nums causes division by zero; returns nums despite None annotation; Unimported `List` |
| `Two Pointers/trapping rain water.py` | Two pointers with left/right maxima | O(n) | O(1) | Unimported `List` |
| `Two Pointers/two_sum_ii_sorted_array.py` | Two pointers on sorted values | O(n) | O(1) | Returns [-1,-1] if no pair; problem guarantees a pair; Unimported `List` |
| `Two Pointers/union of two sorted arrays.py` | Sorted two-way merge with deduplication | O(m+n) | O(m+n) output | — |

## Review notes

- No solution files were modified. These are source reviews, not full judge submissions or exhaustive test results.
- The input contracts for demo snippets and unspecified custom problems need confirmation before treating their edge cases as accepted behavior. Conditional concerns are marked in their rows.