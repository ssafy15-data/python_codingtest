import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

T = int(input())

"""
영준이의 BFS -> BFS 순서로 나오는 순회에서 노드간 거리의 합을 구해라
공통 조상을 구하면 노드 u에서 노드 v까지의 거리는 u-공통조상 거리 + v-공통조상 거리 => root기준 depth[u] - depth[lca] + depth[v] - depth[lca] = depth[u] + depth[v] - 2 * depth[lca]

"""


for tc in range(1, T + 1):
    n = int(input())
    LOG = (n + 1).bit_length()
    tree = [[] for _ in range(n + 1)]
    depth = [0] * (n + 1)
    parent = [[0] * (n + 1) for _ in range(LOG)]

    input_parents = [*map(int, input().split())]  # 2부터
    for child in range(2, n + 1):
        p = input_parents[child - 2]
        tree[p].append(child)
        parent[0][child] = p
    
    # ====================================
    # LCA
    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in tree[cur]:
            depth[nxt] = depth[cur] + 1
            q.append(nxt)
    
    for k in range(1, LOG):
        for v in range(1, n + 1):
            parent[k][v] = parent[k - 1][parent[k - 1][v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if diff & (1 << k):
                u = parent[k][u]
        
        if u == v:
            return u

        for k in range(LOG - 1, -1, -1):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]
        
        return parent[0][u]
    

    # ==============================
    # BFS
    q = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    bfs_route = [1]
    while q:
        cur = q.popleft()
        for nxt in tree[cur]:
            if not visited[nxt]:
                bfs_route.append(nxt)
                q.append(nxt)

    res = 0
    for i in range(n - 1):
        a, b = bfs_route[i], bfs_route[i + 1]
        res += depth[a] + depth[b] - 2 * depth[lca(a, b)]

    print(f'#{tc} {res}')
