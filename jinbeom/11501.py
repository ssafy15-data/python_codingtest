import sys

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

T=int(input())
for _ in range(T):
    n=int(input())
    arr=tuple(map(int,input().split()))
    curr_max=arr[-1]
    ret=0
    for val in arr[n-1::-1]:
        if val>curr_max:
            curr_max=val
        else:
            ret+=curr_max-val
    print(ret)