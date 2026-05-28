from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        양방향으로 최단거리를 코스트를 추가해서 구하자
        바뀌어야 되는 경우엔 cost 1부여
        그 이후 다익스트라해서 dist sum을 하려고 했는데 여러 번 바꾸는 경우가 발생할 수도 있네

        경로 체크가 있긴 해야될듯
        순수 bfs로 하면 될 듯
        """
        INF = int(1e9)

        graph = [[] for _ in range(n + 1)]
        for a, b in connections:
            graph[a].append((b, 1))  # 0부터 돌릴 것이므로 cost는 반대로 부여
            graph[b].append((a, 0))
        
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        res = 0
        while q:
            cur = q.popleft()
            for nxt, nxt_cost in graph[cur]:
                if not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = True
                    if nxt_cost == 1:
                        res += 1
        
        return res
