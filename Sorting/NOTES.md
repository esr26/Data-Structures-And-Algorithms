# Sorting

Use merge sort when a stable O(n log n) worst-case bound or merge-based counting is useful. Use quicksort when average in-place performance is the priority and worst-case O(n²) is acceptable. This folder implements both.

## Divide-and-conquer workflow

1. Stop at a subarray of size zero or one.
2. Divide the range into smaller parts.
3. Recursively sort the parts.
4. For merge sort, merge the sorted halves in order; for quicksort, partition around a pivot before sorting the sides.
5. Return or retain the sorted range and verify duplicates and boundary elements.

**Complexity:** Merge sort takes O(n log n) time and O(n) extra space with array merging. Quicksort averages O(n log n) time and O(log n) recursion space with balanced partitions, but worst-case time and stack depth can reach O(n²) and O(n). Exact space depends on whether the implementation copies slices.

**Pitfalls:** Avoid dropping an element at partition or merge boundaries. Poor pivot choices degrade quicksort. Decide whether equal keys must retain their original order; merge sort can be stable, ordinary quicksort is not.
