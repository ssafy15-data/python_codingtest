import sys
from itertools import combinations

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

n=int(input())
stats=[tuple(map(int,input().split())) for _ in range(n)]
tot=set(range(n))
ret=1e9

for team1 in combinations(range(n-1),n//2):
    team2=tot-set(team1)
    tmp=0
    for x in team1:
        for y in team1:
            tmp+=stats[x][y]
    for x in team2:
        for y in team2:
            tmp-=stats[x][y]
    ret=min(ret,abs(tmp))

print(ret)