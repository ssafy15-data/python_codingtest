import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

# 0: 위로부터, 1: 왼쪽으로부터, 2: 오른쪽으로부터, 3: 최대값
dp_table = [[ [-100]*m for _ in range(n) ] for _ in range(4)]

# 0번째 행
dp_table[3][0][0] = matrix[0][0]
for j in range(1, m):
    dp_table[3][0][j] = dp_table[3][0][j-1] + matrix[0][j]

# 1번째 행부터
for i in range(1, n):

    # 0. 위로부터 이동 (기본값)
    for j in range(m):
        dp_table[0][i][j] = dp_table[3][i-1][j] + matrix[i][j]

    # 1. 왼쪽으로부터 이동 (0.과 비교)
    dp_table[1][i][0] = dp_table[0][i][0]
    for j in range(1, m):
        dp_table[1][i][j] = max(dp_table[0][i][j], dp_table[1][i][j-1] + matrix[i][j])

    # 2. 오른쪽으로부터 이동 (0.과 비교)
    dp_table[2][i][m-1] = dp_table[0][i][m-1]
    for j in range(m-2, -1, -1):
        dp_table[2][i][j] = max(dp_table[0][i][j], dp_table[2][i][j+1] + matrix[i][j])
    
    # 3. 최대값 (1. 2. 비교)
    for j in range(m):
        dp_table[3][i][j] = max(dp_table[1][i][j], dp_table[2][i][j])

print(dp_table[3][n-1][m-1])