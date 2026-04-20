# 최솟값 찾기 - Gold 1

import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

d = []
q = deque()

for i in range(N):
    # 삽입하려는 arr[i]보다 값이 크다면 앞으로 절대 최솟값이 될 수 없으므로 pop
    # while 반복문으로 인해 기존에 queue에 있던 값 중
    # arr[i]보다 큰 값은 존재하지 않게 됨
    # -> 가장 작은 값이 queue의 맨 앞에 위치하게 되고, 순서대로 정렬됨
    while q and q[-1][0] > arr[i]:
        q.pop()
    # 현재 값과 index 함께 삽입
    q.append((arr[i], i))
    # 최솟값의 index가 범위 밖이라면 pop
    if q[0][1] < i-L+1: # 매번 범위가 1씩 움직이므로 while이 아닌 if문으로 처리 가능
        q.popleft()
    # => 현재 범위 중, 가장 작은 값이 queue의 맨 앞에 위치하게 됨

    # 해당 범위의 최솟값 d에 저장
    d.append(q[0][0])

print(*d)