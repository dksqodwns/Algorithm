import sys

T = int(sys.stdin.readline())

numbers = set(int(sys.stdin.readline()) for _ in range(T))

sorted_numbers = sorted(numbers)

for i in sorted_numbers:
    print(i)
