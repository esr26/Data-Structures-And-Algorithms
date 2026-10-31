# Stacks

Use a stack when the most recent unresolved item must be handled first: nested delimiters, expression evaluation, undo-like parsing, or next-greater/smaller-element queries. This folder also includes queue emulation and a frequency stack.

## Monotonic-stack workflow

1. Decide whether the stack should hold increasing or decreasing values, usually by index.
2. Scan items in order.
3. While the new item resolves the top item, pop and compute that item's answer.
4. Push the new item's index after resolving earlier items.
5. Assign the required default to items left unresolved after the scan.

**Complexity:** A monotonic stack is O(n) time and O(n) space because each item enters and leaves once. A basic delimiter or postfix-expression stack also uses O(n) time and O(n) space. The complexity of emulated queues/stacks depends on which operation performs transfers.

**Pitfalls:** Decide whether comparisons are strict so equal values behave correctly. Store indices when distances or widths matter. For histogram areas, use the correct left/right boundary after popping. Check empty-stack access and operator operand order.
