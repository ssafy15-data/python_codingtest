import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, l = map(int, input().split())
a = [*map(int, input().split())]

dq = deque()
res = []

for i in range(n):
    while dq and a[dq[-1]] > a[i]:
        dq.pop()
    
    dq.append(i)
    if dq[0] <= i - l:
        dq.popleft()
    
    res.append(a[dq[0]])
    
print(*res)
