import math
import sys

input = lambda : sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 6)
#
# def dp(remaining):
#     if remaining == 0: return 0
#     if remaining in memo: return memo[remaining]
#     memo[remaining] = min(dp(remaining - k * k) for k in range(int(math.isqrt(remaining)), 0, -1)) + 1
#     return memo[remaining]
#
# memo = {}
n = int(input())
# answer = dp(n)
# print(dp(int(input())))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = 1 + min(dp[i - k*k] for k in range(1, math.isqrt(i) + 1))
print(dp[n])
