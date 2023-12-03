
import sys


def new_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)


N = int(sys.stdin.readline().strip())
if N:
    level_list = []
    for _ in range(N):
        level_list.append(int(sys.stdin.readline().strip()))

    trim = new_round(N * 0.15)
    level_list.sort()
    if trim > 0:
        print(new_round(sum(level_list[trim:-trim]) / len(level_list[trim:-trim])))
    else:
        print(new_round(sum(level_list) / len(level_list)))
else:
    print(0)
