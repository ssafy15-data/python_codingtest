# import sys
# sys.stdin = open("sample.txt", "r")

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
humans = [i for i in range(n)]

# 두 집합이 주어졌을 때의 점수 차이 계산
def cal_diff(comb1, comb2):
    comb_len = len(comb1)

    sum_comb1 = 0
    for idx1 in range(comb_len):
        human1 = comb1[idx1]
        for idx2 in range(idx1+1, comb_len):
            human2 = comb1[idx2]
            sum_comb1 += matrix[human1][human2] + matrix[human2][human1]
    
    sum_comb2 = 0
    for idx1 in range(comb_len):
        human1 = comb2[idx1]
        for idx2 in range(idx1+1, comb_len):
            human2 = comb2[idx2]
            sum_comb2 += matrix[human1][human2] + matrix[human2][human1]

    return abs(sum_comb1-sum_comb2)

comb = []
min_diff = [1e9]
visited = [False] * n

# 집합을 만들고, 만들었을 경우 바로 점수 차이 계산하고 최소값만 남기도록 함.
def combination(start, num):
    if num == 0:
        diff = cal_diff(comb, list(set(humans)-set(comb)))
        min_diff[0] = min(min_diff[0], diff)
        return

    for i in range(start, n):
        visited[i] = True
        comb.append(i)
        combination(i+1, num-1)
        comb.pop()
        visited[i] = False

combination(0, n//2)

print(min_diff[0])
