# Math

Use direct arithmetic when the problem asks for divisibility, digits, primality, or a greatest common divisor. This folder contains Euclid's algorithm, divisor enumeration, primality checks, and digit-processing problems.

## Arithmetic workflow

1. Write down the mathematical property to test or compute.
2. Determine the smallest useful range: divisors need only be checked through `sqrt(n)`.
3. For digits, repeatedly take the last digit with `% 10` and remove it with `// 10`.
4. For GCD, repeatedly replace `(a, b)` with `(b, a % b)` until `b` is zero.
5. Check zero, negative input, and any output-order or overflow rules.

**Complexity:** Euclid's GCD is O(log min(a, b)) time and O(1) space iteratively. Trial division and divisor enumeration take O(√n) time; enumerating divisors needs O(d) output space for d divisors. Digit scans take O(log₁₀ n) time.

**Pitfalls:** Handle n = 0 or 1 explicitly in prime checks. Do not duplicate a square-root divisor. Decide whether sign should be ignored for digit tests, and whether the target language has fixed-width integer limits.
