import sys

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

n=int(input())
arr=[int(input()) for _ in range(n)]

if n==1:
    print(arr[0])
elif n==2:
    print(arr[0]+arr[1])
else:
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=arr[0]+arr[1]
    dp[2]=max(arr[0],arr[1])+arr[2]

    for idx in range(3,n):
        dp[idx]=arr[idx]+max(dp[idx-2],dp[idx-3]+arr[idx-1])

    print(dp[-1])