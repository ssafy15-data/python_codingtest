import sys
from bisect import bisect_left

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

n=int(input())
m=n**2
arr=[]
for _ in range(n):
    arr+=list(map(int,input().split()))
arr.sort()
prefix=[0]*m
prefix[0]=arr[0]
for idx in range(1,m):
    prefix[idx]=prefix[idx-1]+arr[idx]

start,end=0,arr[-1]
ret=0
while start<=end:
    mid=(start+end)//2
    idx=bisect_left(arr,mid)
    if (prefix[idx]-arr[idx]+(m-idx)*mid)*2<prefix[-1]:
        start=mid+1
    else:
        ret=mid
        end=mid-1
print(ret)