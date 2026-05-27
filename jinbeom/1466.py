class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for j, i in connections:
            adj[i].append(j)
            adj[j].append(-i - 1)

        ret = 0
        visit = [False] * n
        visit[0] = True
        q = [0]
        while q:
            now = q.pop()
            for nxt in adj[now]:
                if nxt < 0 and not visit[-nxt - 1]:
                    q.append(-nxt - 1)
                    visit[-nxt - 1] = True
                    ret += 1
                    print(now, -nxt - 1)
                elif nxt > 0 and not visit[nxt]:
                    q.append(nxt)
                    visit[nxt] = True
        return ret
