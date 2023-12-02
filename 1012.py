# import sys

# sys.setrecursionlimit(10 ** 6)  # 재귀함수의 한도를 늘려주기 위해서

# input = sys.stdin.readline  # 이건 좀 더 빠른 입력이 가능하다던데

# MAX = 50 + 10

# # 1. 입력 및 배열 초기화
# T = int(input())  # 테스트 케이스 입력받기

# dirR = [1, -1, 0, 0]  # Row
# dirC = [0, 0, 1, -1]  # Column
# # 상하좌우 모두 돌면서 탐색 해야 하므로 (dirR, dirC)을 정의하기 위해 생성함 (1, 0)이면 좌, (-1,0)이면 우 이런 느낌


# def dfs(y, x):
#     global visited
#     visited[y][x] = True
#     for dirIdx in range(4):  # 상하좌우 모두 확인 함
#         newY = y + dirR[dirIdx]
#         newX = x + dirC[dirIdx]
#         if graph[newY][newX] and not visited[newY][newX]:  # 다시 받은 배열로 확인
#             dfs(newY, newX)


# for _ in range(T):
#     M, N, K = map(int, input().split())  # 배열의 크기 및 배추의 개수 입력받음
#     graph = [[False] * MAX for _ in range(MAX)]  # False로 채워진 그래프
#     # 같은 크기의 방문 여부를 저장해둘 visit 그래프
#     visited = [[False] * MAX for _ in range(MAX)]

# # 2. 그래프 정보 입력
#     for _ in range(K):  # 배추의 정보가 K번 들어와야 해서 K번 반복
#         x, y = map(int, input().split())  # 배추의 좌표 입력
#         graph[y+1][x+1] = True  # 배추가 있는 곳은 True

# # 3. DFS 시작
#     result = 0  # 지렁이 초기화
#     for i in range(1, N+1):  # Y축 만큼 돌고
#         for j in range(1, M+1):  # X축 만큼 돌아서
#             if graph[i][j] and not visited[i][j]:  # 그래프 배열에 배추가 있고, 방문하지 않았다면
#                 dfs(i, j)  # 함수 동작
#                 result += 1  # 지렁이 추가
#     print(result)


# 버전 2

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

MAX = 50 + 10

T = int(input())

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]


def dfs(y, x):
    graph[y][x] = False  # 지나간 곳은 False로 바꿔줌
    for dirIdx in range(4):
        newY = y + dirR[dirIdx]
        newX = x + dirC[dirIdx]
        if graph[newY][newX]:
            dfs(newY, newX)


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]

# 2. 그래프 정보 입력
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y+1][x+1] = True

# 3. DFS 시작
    result = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if graph[i][j]:
                dfs(i, j)
                result += 1
    print(result)
