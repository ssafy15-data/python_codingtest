import sys

input = sys.stdin.readline
# sys.stdin=open('input.txt','r')

n, m = map(int, input().split())
board = [tuple(map(int, input().split())) for _ in range(n)]
dp1 = [[0] * m for _ in range(n)]
dp2 = [[0] * m for _ in range(n)]

dp1[-1][-1] = board[-1][-1]
dp2[-1][-1] = board[-1][-1]

for idx in range(m - 2, -1, -1):
    dp1[n - 1][idx] = dp1[n - 1][idx + 1] + board[n - 1][idx]
    dp2[n - 1][idx] = dp2[n - 1][idx + 1] + board[n - 1][idx]

for row in range(n - 2, -1, -1):
    dp1[row][0] = board[row][0] + max(dp1[row + 1][0], dp2[row + 1][0])
    dp2[row][m - 1] = board[row][m - 1] + max(dp1[row + 1][m - 1], dp2[row + 1][m - 1])

    for col in range(1, m):
        dp1[row][col] = max(dp1[row][col - 1], dp1[row + 1][col], dp2[row + 1][col]) + board[row][col]

    for col in range(m - 2, -1, -1):
        dp2[row][col] = max(dp2[row][col + 1], dp1[row + 1][col], dp2[row + 1][col]) + board[row][col]

print(max(dp1[0][0], dp2[0][0]))
