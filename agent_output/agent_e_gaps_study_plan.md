# Agent E — Coverage gaps and study plan

## Coverage against the requested topic list

The repo has 157 Python solution files across 10 topic folders. Folder counts are a measure of stored solutions, not proof of mastery or correctness. Several patterns appear inside other folders; “no dedicated files” does not mean the concept has never been used.

| Requested topic | Repo evidence | Assessment |
|---|---|---|
| Arrays | 30 files in `Array & Hashing/` | Substantial coverage |
| Strings | 13 files in `Strings/` | Covered |
| Hashing | `Array & Hashing/` includes `subarray sum equals k.py` and `longest-consecutive-sequence.py` | Covered within arrays; no separate folder |
| Two pointers | 11 files in `Two Pointers/` | Covered |
| Sliding window | 9 files in `Sliding Window/` | Covered |
| Linked lists | No dedicated folder or solution | Missing |
| Stacks and queues | 15 files in `Stacks/`, including both stack/queue conversion problems; graph BFS also uses queues | Stacks covered; standalone queue practice is thinner |
| Trees | No dedicated folder or solution | Missing |
| Heaps | No dedicated folder; weighted graph algorithms use priority queues | Weak as a standalone topic |
| Graphs | 42 files in `Graph/` | Substantial coverage |
| Dynamic programming | No dedicated folder; some graph/string solutions may use DP ideas | Missing as a dedicated topic |
| Greedy | No dedicated folder; some two-pointer/scheduling solutions use greedy choices | Weak as a standalone topic |
| Backtracking | No dedicated folder or clear combinatorial backtracking series | Missing |
| Tries | No dedicated folder or solution | Missing |
| Bit manipulation | 1 file in `Bit Manupulation/`: `Single Number.py` | Weak; folder spelling is existing repo spelling |

The largest coverage gaps are linked lists, trees, dynamic programming, backtracking, and tries. Heaps, greedy, and bit manipulation deserve a focused practice sequence. Queue design can be folded into the existing stacks/queues practice rather than treated as another full gap.

## Problem bank for the eight gaps

Each problem title, number, and difficulty below was checked against its linked LeetCode problem page on 2026-10-31. These are recommendations for future practice, not claims that the repo already contains solutions. The recommendations are ordered from foundations to harder applications within each topic.

### Linked lists

1. [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — Easy; pointer reversal.
2. [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — Easy; dummy head and merge.
3. [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) — Easy; fast and slow pointers.
4. [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) — Medium; fixed pointer gap.
5. [143. Reorder List](https://leetcode.com/problems/reorder-list/) — Medium; midpoint, reverse, weave.

### Trees

1. [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — Easy; recursive DFS.
2. [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) — Easy; subtree recursion.
3. [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — Medium; BFS queue.
4. [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) — Medium; valid bounds.
5. [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) — Medium; BST ordering.

### Heaps and priority queues

1. [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) — Medium; bounded heap.
2. [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — Medium; frequency map plus heap/buckets.
3. [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) — Medium; bounded max-heap.
4. [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) — Hard; two heaps.
5. [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) — Hard; heap of current list heads.

### Dynamic programming

1. [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) — Easy; one-dimensional recurrence.
2. [198. House Robber](https://leetcode.com/problems/house-robber/) — Medium; take/skip state.
3. [62. Unique Paths](https://leetcode.com/problems/unique-paths/) — Medium; grid recurrence.
4. [322. Coin Change](https://leetcode.com/problems/coin-change/) — Medium; minimum-cost state.
5. [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) — Medium; sequence DP and later binary-search optimization.

### Greedy

1. [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/) — Easy; sort and match.
2. [55. Jump Game](https://leetcode.com/problems/jump-game/) — Medium; farthest reachable index.
3. [134. Gas Station](https://leetcode.com/problems/gas-station/) — Medium; restart after deficit.
4. [763. Partition Labels](https://leetcode.com/problems/partition-labels/) — Medium; last occurrence boundary.
5. [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) — Medium; greedy frontier layers.

### Backtracking

1. [78. Subsets](https://leetcode.com/problems/subsets/) — Medium; include/exclude choices.
2. [46. Permutations](https://leetcode.com/problems/permutations/) — Medium; used-element tracking.
3. [39. Combination Sum](https://leetcode.com/problems/combination-sum/) — Medium; choose/reuse/undo.
4. [79. Word Search](https://leetcode.com/problems/word-search/) — Medium; grid search with visited state.
5. [51. N-Queens](https://leetcode.com/problems/n-queens/) — Hard; column/diagonal constraints.

### Tries

1. [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) — Medium; insert, search, prefix.
2. [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) — Medium; wildcard branching.
3. [648. Replace Words](https://leetcode.com/problems/replace-words/) — Medium; shortest stored prefix.
4. [677. Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) — Medium; prefix aggregate and updates.
5. [212. Word Search II](https://leetcode.com/problems/word-search-ii/) — Hard; trie-guided backtracking.

### Bit manipulation

1. [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) — Easy; clear the lowest set bit.
2. [231. Power of Two](https://leetcode.com/problems/power-of-two/) — Easy; one-bit property.
3. [338. Counting Bits](https://leetcode.com/problems/counting-bits/) — Easy; bit-count recurrence.
4. [137. Single Number II](https://leetcode.com/problems/single-number-ii/) — Medium; bit counts modulo three.
5. [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) — Medium; common binary prefix.

## Two-week starter plan

The problem bank has 40 problems. This 14-day first pass selects 24 across all eight gaps; the rest remain a follow-up queue. On each practice day, record the invariant/state, implement in Python, test empty/minimal and boundary inputs, then write one mistake note. Use Day 7 and Day 14 to re-solve without looking at the original code.

| Day | Focus | Problems |
|---|---|---|
| 1 | Linked-list pointers | 206, 21 |
| 2 | Linked-list traversal | 141, 19 |
| 3 | Tree recursion | 104, 226 |
| 4 | Tree BFS and BST invariant | 102, 98 |
| 5 | Heap selection | 215, 347 |
| 6 | Heap and first DP state | 973, 70 |
| 7 | Review | Re-solve one linked-list, one tree, and one heap problem; log failures |
| 8 | Basic DP | 198, 62 |
| 9 | Greedy choice | 455, 55 |
| 10 | Greedy boundary and backtracking | 763, 78 |
| 11 | Backtracking state | 46, 39 |
| 12 | Trie operations | 208, 211 |
| 13 | Trie application and bits | 648, 191 |
| 14 | Review | Re-solve one DP, one greedy, one backtracking, one trie, and one bit problem; pick the next queue |

The next cycle should prioritize the remaining problems from each gap, especially 295/23 (heaps), 322/300 (DP), 51 (backtracking), 212 (tries), and 137/201 (bits). For queue-specific follow-up, revisit the existing `Stacks/implement-queue-using-stacks.py` and `Graph/Iterative BFS.py` before adding another design problem.
