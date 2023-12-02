import sys

N = int(sys.stdin.readline())
word_set = set()
for _ in range(N):
    word_set.add(sys.stdin.readline().strip())

sort_set = sorted(word_set, key=lambda x: (len(x), x))

for i in sort_set:
    print(i)