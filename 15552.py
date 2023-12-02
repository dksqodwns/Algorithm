import sys

T = int(input())
result = []

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

print('\n'.join(map(str, result)))
