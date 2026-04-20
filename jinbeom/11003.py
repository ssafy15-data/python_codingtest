import sys
from collections import deque

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

n,l=map(int,input().split())
arr=tuple(map(int,input().split()))
q=deque()
ret=[]

for idx in range(n):
    while q and arr[q[-1]]>=arr[idx]:
        q.pop()
    q.append(idx)
    while q[0]<idx-l+1:
        q.popleft()
    ret.append(arr[q[0]])

print(*ret)