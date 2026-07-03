import math

def isPrime(n):

    if n <= 1:
        return "Not Prime"

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"
