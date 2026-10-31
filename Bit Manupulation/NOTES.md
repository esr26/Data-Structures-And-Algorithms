# Bit Manipulation

The current folder contains **Single Number**, where every value except one appears twice. XOR is useful because equal values cancel: `x ^ x = 0` and `x ^ 0 = x`.

## XOR workflow

1. Confirm that exactly one value occurs once and every other value occurs twice.
2. Start an accumulator at zero.
3. XOR each input value into the accumulator.
4. Return the accumulator, which is the unpaired value.

**Complexity:** O(n) time and O(1) extra space.

**Pitfalls:** The method depends on the frequency promise. It does not directly solve variants where other values occur three times or two values are unique. Python handles negative integers here because XORing identical values still cancels.
