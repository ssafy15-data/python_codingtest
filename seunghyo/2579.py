N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

DP = [0 for _ in range(301)]

if N >= 1:
    DP[0] = arr[0]
if N >= 2:
    DP[1] = arr[0] + arr[1]
if N >= 3:
    DP[2] = max(arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, N):
    DP[i] = max(DP[i-3] + arr[i-1] + arr[i], DP[i-2] + arr[i])

print(DP[N-1])