import sys

input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

"""
큰 제곱수부터 빼서 남은 수가 제곱수인지 체크
dp[남은 수] => dp[i] = min(dp[i - j^2]) + 1
"""

squares = [x**2 for x in range(int(50001**0.5))]

dp = [INF] * (50001)
dp[0] = 0
for x in squares:
    dp[x] = 1

n = int(input())
max_idx = int(n**0.5)

for i in range(1, n + 1):
    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[n])
