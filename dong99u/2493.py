import sys; input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

stack = []
result = []

for i in range(n):
    if not stack:
        stack.append((i, l[i]))
        result.append(0)
        continue
    while stack and stack[-1][1] < l[i]:
        stack.pop()
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)
    stack.append((i, l[i]))

print(*result)

