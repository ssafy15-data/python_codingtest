# 시간초과

# 모든 경우의 수를 구하되, 가지치기 + 메모이제이션
# 누적합을 이용해서, 지금부터 max로 더해도 도달하지 못하거나,
# min을 이용해서, 제일 작은 수만 더해도 초과해버리는 경우, 가지치기

n, m, h = map(int, input().split())

blocks = [sorted(list(map(int, input().split()))) for _ in range(n)]

dp_table = [ {} for _ in range(n) ]

max_cums = [] # 해당 차례 사람부터 마지막 사람까지 쌓을 수 있는 최대 높이 (점점 줄어들고 마지막은 마지막 사람의 최대값)
mins = [] # 해당 차례 사람부터 마지막 사람까지 가진 것들 중 가장 작은 높이 (점점 커지고 마지막은 마지막 사람의 최소값)

temp_max = 0
temp_min = 1000
for i in range(n):
    temp_max += max(blocks[i])
    max_cums[i] = temp_max

    temp_min = min(temp_min, min(blocks[i]))
    mins[i] = temp_min

def dp(human, height):

    if height > max_cums[human]:
        return 0
    if height < mins[human]:
        return 0
    
    if human == n-1:
        if height in blocks[human]:
            return 1
        else:
            return 0

    cnt = 0
    dp_table[human+1][height] = dp_table[human+1].get(height, dp(human+1, height))
    cnt += dp_table[human+1][height]
    for block in blocks[human+1]:
        if block == height:
            dp_table[human+1][height-block] = 1
            cnt += 1
            break
        elif block > height:
            break
        else:
            dp_table[human+1][height-block] = dp_table[human+1].get(height-block, dp(human+1, height-block))
            cnt += dp_table[human+1][height-block]
    
    return cnt

print(dp(0, h))

# dp(human, height): human 인덱스의 학생부터 시작해서 height를 만들 수 있는 경우의 수

# dp(0, h) 
# = dp_table[0][h]
# = dp(1, h-block_1) + dp(1, h-block_2) + ... + dp(1, h-block_k)

# dp(1, h-b)
# = dp_table[1][h-b]
# = dp(2, h-b-block_1) + dp(2, h-b-block_2) + ... + dp(2, h-b-block_k)
