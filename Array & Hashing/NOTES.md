# Array & Hashing

Use a set or map when membership, frequency, or a previously seen prefix matters. Use an in-place array scan when the answer depends on order or positions. This folder also has interval merging, matrix traversal, Kadane's algorithm, merge-sort counting, and Floyd cycle detection for a duplicate value without modifying the array.

## Prefix-hash workflow

1. Define a prefix state (sum or XOR) before scanning.
2. Seed the map with the empty prefix when counting subarrays.
3. For each value, update the prefix.
4. Look up the complement needed to form the target and add its frequency to the answer.
5. Record the current prefix after the lookup; for a longest-length variant, keep the earliest index instead.

**Complexity:** A single hash scan is expected O(n) time and O(n) space. In-place scans such as Kadane's algorithm and Floyd cycle detection are O(n) time and O(1) extra space. Sorting intervals or merge-sort counts take O(n log n) time; a matrix scan takes O(rows × columns).

**Pitfalls:** Seed the empty prefix correctly. Do not confuse counting frequencies with saving the first index. Include negative numbers when choosing an algorithm: a shrinking sum window is not generally valid with them. Check whether “in place” permits a result array.
