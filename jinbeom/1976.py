import sys

input = sys.stdin.readline
# sys.stdin=open('input.txt','r')

n, m = int(input()), int(input())
graph = []
for _ in range(n):
    tmp = input().split()
    graph.append(tuple(i for i, j in enumerate(tmp) if j == '1'))

idx = 0
ret = dict()

for start in range(n):
    if start in ret: continue
    q = [start]
    ret[start] = idx
    while q:
        now = q.pop()
        for nxt in graph[now]:
            if nxt not in ret:
                q.append(nxt)
                ret[nxt] = idx
    idx += 1

route = tuple(map(int, input().split()))
result = 'YES'
idx = ret[route[0] - 1]
for i in range(1, m):
    if idx != ret[route[i] - 1]:
        result = 'NO'
        break

print(result)
