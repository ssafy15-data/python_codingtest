N, M = map(int, input().split())

INF = 1e9
DP = [[-INF for _ in range(M)] for _ in range(N)]
info = []

for _ in range(N):
    info.append(list(map(int, input().split())))

DP[0][0] = info[0][0]

for idx in range(1, M):
    DP[0][idx] = DP[0][idx-1] + info[0][idx]


for i in range(1, N):
    LtoR = [-INF for _ in range(M)]
    RtoL = [-INF for _ in range(M)]
    for j in range(M):
        if j == 0:
            LtoR[j] = DP[i-1][j] + info[i][j]
        else:
            LtoR[j] = max(DP[i-1][j] + info[i][j], LtoR[j-1] + info[i][j])

    for n in range(M-1, -1, -1):
        if n == M-1:
            RtoL[n] = DP[i-1][n] + info[i][n]
        else:
            RtoL[n] = max(DP[i-1][n] + info[i][n], RtoL[n+1] + info[i][n])

    for idx in range(M):
        DP[i][idx] = max(LtoR[idx], RtoL[idx])


print(DP[N-1][M-1])
