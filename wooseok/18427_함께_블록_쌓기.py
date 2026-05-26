import sys

input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

n, m, h = map(int, input().split())

dp = [[0] * (h + 1) for _ in range(n + 1)]  # i번째 학생, j높이
dp[0][0] = 1

for i in range(1, n + 1):
    cur_block = [*map(int, input().split())]
    for j in range(h + 1):
        dp[i][j] = dp[i - 1][j]

        for block in cur_block:
            if j >= block:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - block]) % 10007

print(dp[n][h])
