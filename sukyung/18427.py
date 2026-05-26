# 함께 블록 쌓기 - Gold 4

# N:학생 수, M: 한 학생이 가지는 블록 최대 개수, H: 탑 높이
N, M, H = map(int, input().split())
stu = []
for _ in range(N):
    s = list(map(int, input().split()))
    stu.append(s)

dp = [[0]*(H+1) for _ in range(N+1)]  # dp[0][j]: 아무도 제출 X 경우
# dp[i][j]: i번째 학생들의 높이 j인 탑 만들 수 있는 경우의 수
for i in range(N+1):
    dp[i][0] = 1  # 높이 0, 즉 아무것도 내지 않는 경우의 수는 모두 1이기 때문
'''
i번째 학생: 높이 j가 내가 가지고 있는 블록의 높이보다 작으면 [i-1][j]와 값 동일
 높이 j가 내가 낼 수 있는 블록의 높이보다 크거나 같으면 -> 내 블록 사용 시작
 내가 가지고 있는 블록의 높이를 각각 뺀 경우의 수와 합치면 됨
 [i-1][j] + [i-1][j-block]
'''
for i in range(1, N+1):
    for j in range(1, H+1):
        dp[i][j] = dp[i-1][j]
        for block in stu[i-1]:  # 현재 i번째 학생이 가진 블록 모두 탐색
            if j-block >= 0:  # 현재 블록을 제출할 수 있는 경우(높이>=0)
                dp[i][j] += dp[i-1][j-block]

print(dp[N][H] % 10007)