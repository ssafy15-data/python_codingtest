# 영준이의 진짜 BFS
from collections import deque
 
T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    nodes = list(map(int, input().split()))
    depths = [0 for _ in range(N + 1)]
 
    queue_info = [[] for _ in range(N + 1)]
    queue_info[0].append(1)
 
    for i in range(N-1):
        parent = nodes[i]
        queue_info[parent].append(i + 2)
        depths[i+2] = depths[parent] + 1
 
    LOG = 17
    up = [[0] * (N + 1) for _ in range(LOG)]
     
    up[0][1] = 1  
    for i in range(N - 1):
        up[0][i + 2] = nodes[i]
     
    for k in range(1, LOG):
        for v in range(1, N + 1):
            up[k][v] = up[k-1][up[k-1][v]]
 
    def find_root(a, b):
        if depths[a] < depths[b]:
            a, b = b, a
         
        diff = depths[a] - depths[b]
        for k in range(LOG):
            if (diff >> k) & 1:
                a = up[k][a]
         
        if a == b:
            return a
         
        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]
         
        return up[0][a]
 
    total_distance = 0
    current_pos = 1
 
    queue = deque()
    queue.append(0)
 
    while queue:
        current = queue.popleft()
        q_root = find_root(current, current_pos)
        total_distance += (depths[current_pos] + depths[current] - depths[q_root] * 2)
        current_pos = current
        for dep in queue_info[current]:
            queue.append(dep)
 
    print(f"#{test_case} {total_distance}")