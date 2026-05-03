import sys

input = lambda: sys.stdin.readline().rstrip()

"""
N, M <= 1000

위쪽 이동 불가 -> i행에서 최대한 가치 파밍. -> 각 행마다 [j]를 시점으로 해서 최대 가치를 얻을 수 있도록 구하기
갔던 곳 이동 불가 -> 좌 / 우 체크

dp i행 기준
왼쪽에서 출발
l[j] = max(dp[i - 1][j], l[j - 1]) + grid[i][j]

오른쪽에서 출발
r[j] = max(dp[i - 1][j], r[j + 1]) + grid[i][j]

dp[i][j] = max(l[j], r[j])
"""

# main code
n, m = map(int, input().split())

dp = [[0] * m for _ in range(n)]
grid = [[*map(int, input().split())] for _ in range(n)]

# 1, 1 시작 -> 무조건 오른쪽
dp[0][0] = grid[0][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + grid[0][j]

for i in range(1, n):
    l = [0] * m
    for j in range(m):
        if j == 0:
            l[j] = dp[i - 1][j] + grid[i][j]
        else:
            l[j] = max(dp[i - 1][j], l[j - 1]) + grid[i][j]
    
    r = [0] * m
    for j in range(m - 1, -1, -1):
        if j == m - 1:
            r[j] = dp[i - 1][j] + grid[i][j]
        else:
            r[j] = max(dp[i - 1][j], r[j + 1]) + grid[i][j]
    
    for j in range(m):
        dp[i][j] = max(l[j], r[j])

print(dp[n - 1][m - 1])
