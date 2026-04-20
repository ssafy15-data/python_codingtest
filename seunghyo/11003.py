import sys
from collections import deque

input = sys.stdin.readline


N, L = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque()
find = []

#print(arr)
for idx in range(N):
    #print(queue, arr[idx])
    while queue and arr[queue[-1]] > arr[idx]:
        queue.pop()

    queue.append(idx)
    if queue[0] <= idx - L:
        queue.popleft()

    find.append(arr[queue[0]])


print(*find)