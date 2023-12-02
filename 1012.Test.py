import sys

sys.setrecursionlimit = 10 ** 6
input = sys.stdin.readline
MAX = 60

T = int(input())

for _ in range(T):
    M, N, K = map(int, input())
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    for _ in range(K):
        x, y = map(int, input().split())
