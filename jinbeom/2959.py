class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        adj = [[1001] * n for _ in range(n)]
        for u, v, w in roads:
            adj[u][v] = min(adj[u][v], w)
            adj[v][u] = min(adj[v][u], w)

        ret = 0
        for k in range(1 << n):
            dist = [[int(1e9)] * n for _ in range(n)]
            curr = set()
            for i in range(n):
                if k & (1 << i): curr.add(i)
                dist[i][i] = 0
            for u in curr:
                for v in curr:
                    if adj[u][v] != 1001: dist[u][v] = adj[u][v]
            for p in curr:
                for q in curr:
                    for r in curr:
                        dist[q][r] = min(dist[q][p] + dist[p][r], dist[q][r])

            def check():
                for p in curr:
                    for q in curr:
                        if dist[p][q] > maxDistance: return 0
                return 1

            ret += check()
        return ret
