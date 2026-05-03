from collections import deque, defaultdict
from itertools import product

"""
경우의 수
type^k => 3^10
bfs => n => 100
3^10 * 100 ~= 5900k ~= 0.06sec

완탐 가능
"""

def bfs(graph, infected, ptype):
    # 현재 감염된 노드들에서 ptype 간선으로만 이동 가능한 노드 전부 추가
    q = deque([node for node in infected])
    while q:
        node = q.popleft()
        for neighbor, t in graph[node]:
            if ptype == t and neighbor not in infected:
                infected.add(neighbor)
                q.append(neighbor)
    return infected

def solution(n, infection, edges, k):
    graph = defaultdict(list)
    for u, v, t in edges:
        graph[u].append((v, t))
        graph[v].append((u, t))
    
    res = 1
    for sequence in product([1, 2, 3], repeat=k):
        # 파이프를 여는 것은 항상 같거나 그 이상으로 좋음
        # 따라서 k번으로 고정시켜도 됨
        infected = {infection}
        for ptype in sequence:
            infected = bfs(graph, infected, ptype)
        res = max(res, len(infected))

    return res