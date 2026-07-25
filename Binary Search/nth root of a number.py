def nthRoot(n, m):
    left = 1
    right = m

    while left <= right:

        mid = (left + right) // 2

        if mid ** n == m:
            return mid

        if mid ** n < m:
            left = mid + 1
        else:
            right = mid - 1

    return -1
