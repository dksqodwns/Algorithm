N = int(input())

dp = [0] * (N + 1)
score = [0] * (N + 1)

for i in range(1, N + 1):
    score[i] = int(input())
if N == 1:
    print(score[1])
elif N == 2:
    print(sum(score[:3]))
elif N > 2:
    dp[1] = score[1]
    dp[2] = score[1] + score[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + score[i], dp[i - 3] + score[i - 1] + score[i])

    print(dp[-1])
