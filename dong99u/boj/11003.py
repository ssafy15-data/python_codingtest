import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque

'''
Q = 빈 큐 (값, 인덱스) 리스트 -> Q[0]은 항상 최솟값 유지
arr 를 모두 순회하면서 만약 new가 Q[-1]보다 작다면(new < Q[-1]) 그 Q에 있는 값들은 출력될 일이 없음 (빼기)
'''

MAX_SIZE = 10 ** 6

n, l = map(int, input().split())
arr = list(map(int, input().split()))

Q = deque()
result = []
for i in range(n):
    # 윈도우 벗어난 원소 제거 (앞에서)
    if Q and i - Q[0][1] >= l:
        Q.popleft()
    # 새 원소보다 큰 원소 제거 (뒤에서)
    while Q and arr[i] < Q[-1][0]:
        Q.pop()
    Q.append((arr[i], i))
    result.append(Q[0][0])  # 항상 실행

print(*result)