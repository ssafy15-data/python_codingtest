N = int(input())
square = [i * i for i in range(1, 250) if i * i <= N]
result = set()
dp = [5] * (N + 1)

for i in range(len(square)):
    for j in range(i, len(square)):
        if square[i] + square[j] <= N:
            dp[square[i] + square[j]] = 2
for s in square:
    dp[s] = 1

if dp[N] == 1 or dp[N] == 2:
    print(dp[N])
else:
    ret = 4
    for i in range(1, N // 2 + 1):
        ret = min(dp[i] + dp[N - i], ret)
    print(ret)
