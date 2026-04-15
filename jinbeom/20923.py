import sys
from collections import deque

input=sys.stdin.readline
# sys.stdin=open('input.txt','r')

def halligalli():
    n,m = map(int,input().split())

    do_deck = deque()
    su_deck = deque()

    for _ in range(n):
        x,y=map(int,input().split())
        do_deck.append(x)
        su_deck.append(y)
        
    do_ground = deque()
    su_ground = deque()

    for turn in range(m):
        if turn % 2 == 0:
            do_ground.append(do_deck.pop())
            if not do_deck:
                print("su")
                return
        else:
            su_ground.append(su_deck.pop())
            if not su_deck:
                print("do")
                return

        do_top = do_ground[-1] if do_ground else 0
        su_top = su_ground[-1] if su_ground else 0

        if do_top == 5 or su_top == 5:
            if su_ground:
                do_deck.extendleft(su_ground)
                su_ground.clear()
            if do_ground:
                do_deck.extendleft(do_ground)
                do_ground.clear()

        elif do_ground and su_ground and do_top + su_top == 5:
            if do_ground:
                su_deck.extendleft(do_ground)
                do_ground.clear()
            if su_ground:
                su_deck.extendleft(su_ground)
                su_ground.clear()

    if len(do_deck) > len(su_deck):
        print("do")
    elif len(do_deck) < len(su_deck):
        print("su")
    else:
        print("dosu")


halligalli()