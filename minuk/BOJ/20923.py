import sys;input=lambda:sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
ary1 = deque()
ary2 = deque()

for i in range(N):
    a, b = map(int, input().split())
    ary1.append(a)
    ary2.append(b)

win = 0
left, right = deque([]), deque([])
for i in range((M + 1) // 2):
    # print(ary1, ary2)
    # print(left, right)
    left.append(ary1.pop())
    if (not ary1):
        win = 2
        break
    if (left[-1] == 5):
        while (right):
            ary1.appendleft(right.popleft())
        while (left):
            ary1.appendleft(left.popleft())
    elif (right and left[-1] + right[-1] == 5):
        while (left):
            ary2.appendleft(left.popleft())
        while (right):
            ary2.appendleft(right.popleft())

    if (M % 2 and i == M // 2): break
    right.append(ary2.pop())
    if (not ary2):
        win = 1
        break
    if (right[-1] == 5):
        while (right):
            ary1.appendleft(right.popleft())
        while (left):
            ary1.appendleft(left.popleft())
    elif (left and left[-1] + right[-1] == 5):
        while (left):
            ary2.appendleft(left.popleft())
        while (right):
            ary2.appendleft(right.popleft())

if (not win):
    if (len(ary1) > len(ary2)): win = 1
    elif (len(ary1) < len(ary2)): win = 2

res = {0: "dosu", 1: "do", 2: "su"}
print(res[win])