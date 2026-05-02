import sys;input=lambda:sys.stdin.readline().rstrip()

stack = [(int(1e9), 0)]
N = int(input())
ary = [*map(int, input().split())]
res = []
for i in range(N):
    val = ary[i]
    while (stack and stack[-1][0] < val):
        stack.pop()
    res.append(stack[-1][1])
    stack.append((val, i + 1))
print(*res)