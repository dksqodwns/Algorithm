num = map(int, input().split())

arr = list(num)
secondArr = []
result = 0
for i in range(len(arr)):
    secondArr.append(arr[i] ** 2)

print(secondArr)
for i in range(len(secondArr)):
    result += secondArr[i]

print(result % 10)
