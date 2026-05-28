class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        """
        조합 만들어서 최단거리 구해고, 최단거리가 maxDistance보다 작게 모두 갈 수 있는 개수
        n <= 10
        => bitmasking + floyd-warshall 2^n * n^3
        """

        INF = int(1e6)

        res = 0

        for mask in range(1 << n):
            dist = [[INF] * n for _ in range(n)]
            for x in range(n):
                dist[x][x] = 0

            for u, v, w in roads:
                if (mask & (1 << u)) and (mask & (1 << v)):
                    if dist[u][v] > w:
                        dist[u][v] = w
                        dist[v][u] = w
            
            for k in range(n):
                if not (mask & (1 << k)):
                    continue
                
                for i in range(n):
                    if not (mask & (1 << i)):
                        continue
                    for j in range(n):
                        if not (mask & (1 << j)):
                            continue
                        
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
            
            # 조건 확인
            flag = True
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                for j in range(n):
                    if not (mask & (1 << j)):
                        continue
                    if dist[i][j] > maxDistance:
                        flag = False
                        break
                
                if not flag:
                    break
            
            if flag:
                res += 1
        
        return res
