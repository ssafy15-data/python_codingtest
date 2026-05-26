import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

n, m = map(int, input().split())

su = deque()
do = deque()
for _ in range(n):
    a, b = map(int, input().split())
    do.appendleft(a)
    su.appendleft(b)

su_ground = deque()
do_ground = deque()

for i in range(m):
    if (i & 1) == 0:  # do turn
        if not do:
            print('su')
            sys.exit()
        do_ground.append(do.popleft())
        if not do:
            print('su')
            sys.exit()
        
    else:
        if not su:
            print('do')
            sys.exit()
        su_ground.append(su.popleft())
        if not su:
            print('do')
            sys.exit()
    
    if (do_ground and do_ground[-1] == 5) or (su_ground and su_ground[-1] == 5):
        while su_ground:
            do.append(su_ground.popleft())
        while do_ground:
            do.append(do_ground.popleft())
    elif su_ground and do_ground and (su_ground[-1] + do_ground[-1] == 5):
        while do_ground:
            su.append(do_ground.popleft())
        while su_ground:
            su.append(su_ground.popleft())

if len(do) == len(su):
    print('dosu')
elif len(do) > len(su):
    print('do')
else:
    print('su')
