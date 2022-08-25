m, n = list(map(int, input().split()))
pro = list(map(int, input().split()))
score = list(map(int, input().split()))
dp = [[0] * (n  + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    dp[i][0] = score[i - 1] * pro[i - 1] / 100 + dp[i - 1][0]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + score[i - 1], dp[i - 1][j] + score[i - 1] * pro[i - 1] / 100)
# print(dp)
print("{:.2f}".format(dp[m][n]))