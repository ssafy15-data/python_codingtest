from itertools import combinations
N = int(input())
synergy = []

for _ in range(N):
    synergy.append(list(map(int, input().split())))

arr = [i for i in range(N)]
team_comb = list(combinations(arr, N // 2))
team_n = len(team_comb)
min_gap = 101

for idx in range(team_n // 2):
    A = team_comb[idx]
    B = team_comb[team_n - idx - 1]

    A_synergy = 0
    B_synergy = 0

    for i in range(len(A)-1):
        player1 = A[i]
        player2 = B[i]
        for j in range(i+1, len(A)):
            player3 = A[j]
            player4 = B[j]
            A_synergy += synergy[player1][player3] + synergy[player3][player1]
            B_synergy += synergy[player2][player4] + synergy[player4][player2]

    min_gap = min(abs(A_synergy - B_synergy), min_gap)

print(min_gap)


