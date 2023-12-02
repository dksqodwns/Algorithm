N = int(input())

input_score = list(map(int, input().split()))
newScore = []
for i in input_score:
    max_score = max(input_score)
    score = (i / max_score) * 100
    newScore.append(score)

print(newScore)

print(sum(newScore) / len(newScore))
