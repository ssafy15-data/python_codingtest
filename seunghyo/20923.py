import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dodo = deque()
suyeon = deque()

for _ in range(N):
    d, s = map(int, input().split())
    dodo.append(d)
    suyeon.append(s)

do_ground = deque()
su_ground = deque()
winner = 0

for turn in range(M):
    if turn % 2 == 0:
        do_ground.append(dodo.pop())
        if len(dodo) == 0:
            winner = "su"
            break
    else:
        su_ground.append(suyeon.pop())
        if len(suyeon) == 0:
            winner = "do"
            break

    if (do_ground and do_ground[-1] == 5) or (su_ground and su_ground[-1] == 5):
        dodo.extendleft(su_ground)
        su_ground.clear()
        dodo.extendleft(do_ground)
        do_ground.clear()
        
    elif do_ground and su_ground and do_ground[-1] + su_ground[-1] == 5:
        suyeon.extendleft(do_ground)
        do_ground.clear()
        suyeon.extendleft(su_ground)
        su_ground.clear()

if winner == 0:
    if len(dodo) > len(suyeon):
        winner = "do"
    elif len(suyeon) > len(dodo):
        winner = "su"
    else:
        winner = "dosu"

print(winner)