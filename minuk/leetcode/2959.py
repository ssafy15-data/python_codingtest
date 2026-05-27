class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        mat = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            mat[i][i] = 0

        for a, b, c in roads:
            mat[a][b] = min(mat[a][b], c)
            mat[b][a] = min(mat[b][a], c)
        
        res = 0
        for mask in range(1 << n):
            mat_copy = [mat[i][:] for i in range(n + 1)]
            
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        now_mask = (1 << k) | (1 << i) | (1 << j)
                        if ((mask & now_mask) == now_mask):
                            mat_copy[i][j] = min(mat_copy[i][j], mat_copy[i][k] + mat_copy[k][j])
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if ((mask & (1 << i)) and (mask & (1 << j))):
                        cnt = max(cnt, mat_copy[i][j])
            res += 1 if (cnt <= maxDistance) else 0
        
        return res