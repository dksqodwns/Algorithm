import sys

N = int(sys.stdin.readline().strip())
five_bag = N // 5

while five_bag >= 0:
    left = N - five_bag * 5
    if left % 3 == 0:
        three_bag = left // 3
        print(five_bag + three_bag)
        break
    five_bag -= 1
else:
    print(-1)
