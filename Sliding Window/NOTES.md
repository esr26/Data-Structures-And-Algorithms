# Sliding Window

Use a window for contiguous subarrays or substrings when adding the next item and removing the left item lets you maintain the needed state. This folder includes fixed-size windows, variable-size character-count windows, and a monotonic deque for window maxima.

## Window workflow

1. Define the invariant: valid window, required frequencies, running sum, or maximum candidate.
2. Move the right boundary and update the state for its new item.
3. While the window violates its condition, move the left boundary and undo its item's contribution.
4. Record the answer at the point where the invariant guarantees it is valid.
5. For fixed-size windows, remove the old left item when size exceeds k; for maxima, discard deque entries that are out of range or dominated.

**Complexity:** Most two-boundary scans are O(n) time because each boundary moves at most n times. Storage is O(1) for a running sum, O(Σ) for character counts, or O(k) for the monotonic deque. `find-k-closest-elements` may instead use binary search, depending on its implementation.

**Pitfalls:** Do not shrink a sum window on arbitrary negative values. Distinguish “at most” from “exactly” constraints. Check when to update the answer and whether duplicate frequencies remain valid when a character leaves.
