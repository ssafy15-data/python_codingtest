from collections import deque

n, m = map(int, input().split())

do = deque([])
su = deque([])

for _ in range(n):
    num1, num2 = map(int, input().split())
    do.append(num1)
    su.append(num2)

do_ground = []
su_ground = []

is_done = False

for i in range(m):
    if i % 2 == 0:
        do_card = do.pop()

        if not do:
            print("su")
            is_done = True
            break

        do_ground.append(do_card)
        if do_card == 5:
            do.extendleft(su_ground + do_ground)
            do_ground = []
            su_ground = []
        elif do_ground and su_ground and do_card + su_ground[-1] == 5:
            su.extendleft(do_ground + su_ground)
            do_ground = []
            su_ground = []
            
    else:
        su_card = su.pop()

        if not su:
            print("do")
            is_done = True
            break
        
        su_ground.append(su_card)
        if su_card == 5:
            do.extendleft(su_ground + do_ground)
            do_ground = []
            su_ground = []
        elif do_ground and su_ground and su_card + do_ground[-1] == 5:
            su.extendleft(do_ground + su_ground)
            do_ground = []
            su_ground = []

if not is_done:
    do_len = len(do)
    su_len = len(su)

    if do_len > su_len:
        print("do")
    elif do_len < su_len:
        print("su")
    else:
        print("dosu")