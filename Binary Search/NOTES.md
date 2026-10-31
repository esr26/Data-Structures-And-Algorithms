# Binary Search

Use binary search when an ordered range or a monotonic yes/no condition lets one comparison discard half the candidates. This folder includes index searches, rotated arrays, answer-space searches, and numeric-precision searches.

## Monotonic-predicate workflow

1. State what a candidate answer means and write a feasibility predicate.
2. Prove the predicate changes only once across the search range.
3. Choose valid lower and upper bounds and decide whether the goal is the first true or last true value.
4. Compute the midpoint, evaluate feasibility, and discard the impossible half.
5. Stop with bounds that preserve the candidate and return the boundary; for floats, stop at the required tolerance.

**Complexity:** Index searches use O(log n) time and O(1) extra space. If feasibility scans n items, answer-space search uses O(n log R) time and O(1) extra space, where R is the integer range. Floating searches use O(n log(R / ε)) for tolerance ε. Matrix and median variants have their own bounds.

**Pitfalls:** Specify inclusive versus exclusive bounds. Test duplicates in rotated arrays, which can force O(n) time. Avoid an unproven monotonic predicate. In numeric searches, guard division and rounding at exact boundaries.
