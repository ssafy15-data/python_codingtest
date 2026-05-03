import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = [[*map(int, input().split())] for _ in range(n)]
members = [*range(n)]

teams = [*combinations(members, n // 2)]

res = int(1e9)

for i in range(len(teams) // 2):
    a_team = teams[i]
    b_team = list(set(members) - set(a_team))
    a, b = 0, 0
    for i, j in combinations(a_team, 2):
        a += s[i][j] + s[j][i]
    for i, j in combinations(b_team, 2):
        b += s[i][j] + s[j][i]
    res = min(res, abs(a - b))

    if res == 0:
        break

print(res)
