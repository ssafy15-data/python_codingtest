import sys;input=lambda:sys.stdin.readline().rstrip()

N = int(input())
ary = [[*map(int, input().split())] for i in range(N)]

def check(t):
    count = 0
    for i in range(N):
        for j in range(N):
            count += min(t, ary[i][j])
    return count >= total

total = sum(sum(ary[i]) for i in range(N)) + 1
total >>= 1
left, right = 0, int(1e7) + 1
ans = right
while (left <= right):
    mid = (left + right) >> 1
    if (check(mid)):
        ans = min(ans, mid)
        right = mid - 1
    else: left = mid + 1
print(ans)


# 값이 매우 크고 최적화 문제인 경우 그냥 구현으로는 풀 수 없음
# 매개 변수 탐색으로 최적화 문제를 선택 문제로 바꾸어야 하는 문제
# 서버실의 컴퓨터 중 절반 이상이 켜지기 위해 필요한 최소 시간 (최적화 문제) -> 시간이 k일 때, 서버실의 컴퓨터 중 절반이 켜지는가? (선택 문제)
# 이때의 k 값이 범위가 정해져있으므로 이분 탐색으로 구할 수 있음
# 그래서 시간은 전체 시뮬레이션 시간 N^2에 이분 탐색 시간 log(1e7)이므로 O(N^2 * log(1e7))이 됨