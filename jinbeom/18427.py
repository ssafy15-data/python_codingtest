import sys

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

N,M,H=map(int,input().split())
block=[set(map(int,input().split())) for _ in range(N)]
dp=[[-1]*(H+1) for _ in range(N)]

def get_dp(n,h):
    if dp[n][h]!=-1: return dp[n][h]
    if n==N-1:
        dp[n][h]=int(h in block[n])+int(h==0)
        return dp[n][h]
    ret=get_dp(n+1,h)
    for b in block[n]:
        if b<=h:
            ret+=get_dp(n+1,h-b)
    dp[n][h]=ret%10007
    return ret

print(get_dp(0,H))