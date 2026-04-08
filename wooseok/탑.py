import sys

input = lambda: sys.stdin.readline().rstrip()

"""
n 50만
n^2 불가

stack (height, idx)
"""

n = int(input())
a = [0] + [*map(int, input().split())]

stack = []
res = []

for i in range(1, n + 1):
    while stack:
        if stack[-1][0] >= a[i]:
            res.append(stack[-1][1])
            break
        else:
            stack.pop()
    
    if not stack:
        res.append(0)
    
    stack.append((a[i], i))

print(*res)