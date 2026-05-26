# 여행 가자
from collections import deque

N = int(input())
M = int(input())

graph = {i: [] for i in range(N)}

for i in range(N):
    info = list(map(int, input().split()))
    for j in range(N):
        if i != j and info[j] == 1:
            graph[i].append(j)

path = list(map(int, input().split()))
path = [x - 1 for x in path]
p_len = len(path)

for idx in range(p_len - 1):
    able = False
    next_p = path[idx + 1]
    visited = [False for _ in range(N)]
    queue = deque()

    queue.append(path[idx])
    visited[path[idx]] = True

    while queue:
        cur = queue.popleft()
        #print(queue, cur, path[idx])
        if cur == next_p:
            able = True
            break
        for g in graph[cur]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True

    if not able:
        print("NO")
        exit()

print("YES")
exit()