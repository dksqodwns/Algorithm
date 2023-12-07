from collections import deque

computers = int(input())
line = int(input())

graph = [[] for i in range(computers + 1)]
visited = [0] * (computers + 1)

for i in range(line):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
visited[1] = 1

q = deque([1])
while q:
    c = q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            q.append(nx)
            visited[nx] = 1
print(sum(visited) - 1)
