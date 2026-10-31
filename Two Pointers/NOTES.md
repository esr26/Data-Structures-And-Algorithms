# Two Pointers

Use two pointers when moving one boundary gives a predictable effect: sorted-pair searches, in-place compaction, merging sorted arrays, or choosing a better container width. This folder also contains 3Sum, 4Sum, trapping rain water, and rotation tasks.

## Opposing-pointer workflow

1. Identify the ordering or invariant that makes pointer movement safe.
2. Initialize left and right at useful boundaries, usually the ends of a sorted range.
3. Evaluate the pair or current interval.
4. Move the pointer whose movement can improve or correct the result.
5. Skip duplicates when listing unique tuples, then stop when the pointers cross.

**Complexity:** A basic opposing or same-direction scan is O(n) time and O(1) extra space. Sorting first makes pair search O(n log n) time; 3Sum is typically O(n²) and 4Sum O(n³) after sorting, excluding output space. Merging with a separate result uses O(n + m) output space.

**Pitfalls:** Pointer movement needs a proof; unsorted inputs may invalidate it. Avoid duplicate tuples after finding a match. Check empty arrays, all-equal arrays, and whether operations must be in place. Container-area and trapped-water moves use different invariants.
