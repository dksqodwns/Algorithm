x, y = map(int, input().split())

matrixA = [list(map(int, input().split())) for _ in range(x)]
matrixB = [list(map(int, input().split())) for _ in range(x)]
result = [[matrixA[i][j] + matrixB[i][j]for j in range(y)] for i in range(x)]


for row in result:
    print(' '.join(map(str, row)))
