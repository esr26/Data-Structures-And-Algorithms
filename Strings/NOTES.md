# Strings

Use character counts for anagrams and frequency comparisons, scans for parsing or nesting, and two-boundary or center expansion for substring questions. The folder includes atoi, palindrome, Roman numeral, rotation, and substring problems.

## Character-scan workflow

1. Define the state needed while scanning: count map, current number, nesting depth, or candidate range.
2. Normalize input only when the problem permits it (for example, whitespace or case).
3. Read each character and update the state according to its role.
4. Check the invariant or record the answer after each update.
5. Handle the end of the string and any empty-input or invalid-character rules.

**Complexity:** A single scan is O(n) time, with O(1) extra space for fixed-size state or O(Σ) for a character map. Sorting by frequency takes O(n log n) with comparison sorting, while center-expansion palindrome search is O(n²) time and O(1) extra space. Costs for built string results include their output size.

**Pitfalls:** Unicode versus fixed alphabet assumptions change count storage. Avoid quadratic repeated string concatenation when building large outputs. For atoi, handle sign, leading spaces, stopping at the first invalid character, and bounds. Keep substring endpoints consistent.
