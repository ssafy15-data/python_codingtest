import sys

input = lambda: sys.stdin.readline().rstrip()

# main code
n = int(input())

dp = [0] * (301)
stair = [0] * (301)
for i in range(1, n + 1):
    stair[i] = int(input())

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1], stair[2]) + stair[3]

# s(n - 1) + d(n - 3) or d(n - 2)

for i in range(4, n + 1):
    dp[i] = max(stair[i - 1] + dp[i - 3], dp[i - 2]) + stair[i]

print(dp[n])