import heapq
import sys

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

def check(target):
    if not q:
        return
    while q:
        if q[0][0]<arr[target]:
            _,idx=heapq.heappop(q)
            ret[idx]=target+1
        else:
            return

n=int(input())
arr=list(map(int,input().split()))
ret=[0]*n
q=[]
for idx in range(n-1,-1,-1):
    check(idx)
    heapq.heappush(q,(arr[idx],idx))
print(*ret)