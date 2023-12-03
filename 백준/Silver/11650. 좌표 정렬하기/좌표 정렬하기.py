import sys

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

new_arr = sorted(arr, key=lambda a: (a[0], a[1]))

for i in new_arr:
    print("{0} {1}".format(i[0], i[1]))
