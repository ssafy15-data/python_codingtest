# 서버실 - Silver 2

import sys
input = sys.stdin.readline

N = int(input())
comp = []
for _ in range(N):
    comp.extend(map(int, input().split()))  # 1차원 배열로 변환
comp_sum = sum(comp)

# 1. 정렬 후 시간과 비교해서 계산
comp.sort()
target = (comp_sum + 1) // 2    # 목표인 컴퓨터 절반 수
t = 0
s = N*N  # len(comp): N*N 칸 이므로
on = 0  # 켜진 컴퓨터 수
i = 0

while on < target:
    # 현재 시간 t보다 큰 값(컴퓨터 수)을 가지고 있는 idx 찾기
    while i < s and comp[i] <= t:
        i += 1
    on += (s - i)   # 이번 t 시간에 켜질 컴퓨터의 수
    t += 1

print(t)


# 2. 이분탐색 사용
# start, end = 0, max(comp)
# # 모든 컴퓨터가 다 켜지는 데 걸리는 최대 시간 = max(comp)
# target = (comp_sum + 1) // 2  # target이 되는 컴퓨터 절반
# t = 0  # 걸린 시간

# while start <= end:
#     mid = (start + end) // 2   # mid: 걸린 시간
#     on = 0  # 켜진 컴퓨터의 수
#     for c in comp:
#         # 만약 쌓인 컴퓨터 수가 걸린 시간보다 작다면 모두 켜졌을 것이고,
#         # 아니라면 걸린 시간만큼만 컴퓨터가 켜졌을 것이다.
#         on += (c if c < mid else mid)
#     if on >= target:    # 절반 이상의 컴퓨터가 켜졌다면
#         t = mid  # 우선 정답으로 걸린 시간인 mid 저장
#         end = mid - 1   # 더 최소 시간이 존재하는지 검사
#     else:   # 아직 절반 미만의 컴퓨터가 켜졌다면
#         start = mid + 1  # start를 옮겨 더 큰 걸린 시간으로 검사 진행

# print(t)