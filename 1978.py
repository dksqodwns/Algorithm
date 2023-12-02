import math

T = int(input())
numbers = list(map(int, input().split()))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


prime_count = sum(is_prime(i) for i in numbers)

print(prime_count)
