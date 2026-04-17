# 계단 오르기 - Silver 3

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
# dp 문제
# step[i][j]: 현재까지 j개의 계단 연속해서 밟고(i번째 계단 포함), 
# i번째 계단 올랐을 때 점수 최댓값
# j = 1 or 2
# step[i][1](j=1): i-1 X, i-2 O
# step[i][2](j=2): i-1 O, i-2 X

step = [[0] * 3 for _ in range(n)]

if n >= 3:
    step[0][1], step[0][2] = arr[0], 0
    step[1][1], step[1][2] = arr[1], arr[0]+arr[1]
    for i in range(2, n):
        step[i][1] = max(step[i-2][1], step[i-2][2]) + arr[i]
        step[i][2] = step[i-1][1] + arr[i]  
    ans = max(step[n-1][1], step[n-1][2])
    
elif n == 2: ans = arr[0] + arr[1]
else: ans = arr[0]  # n==1인 경우
    
print(ans)