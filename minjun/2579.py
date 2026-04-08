n = int(input())
stairs = [int(input()) for _ in range(n)]

# 이전의 연속된 계단을 밟았는가에 대한 차원
# 해당 계단까지 오는데의 최대값
dp_table = [[0]*2 for _ in range(n)]

# 연속된 계단을 밟지 않은 상태의 이전 단계로부터의 최대값 -> 연속된 상태인 1
# 연속된 계단을 밟았거나 밟지 않았거나 2개 이전 단계로부터의 최대값 -> 연속되지 않은 상태인 0

if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0]+stairs[1])
else:
    dp_table[0] = [stairs[0], stairs[0]]
    dp_table[1] = [stairs[1], stairs[0]+stairs[1]]

    for i in range(2, n):
        dp_table[i][0] = max(dp_table[i-2][0], dp_table[i-2][1]) + stairs[i]
        dp_table[i][1] = dp_table[i-1][0] + stairs[i]

    print(max(dp_table[-1][0], dp_table[-1][1]))