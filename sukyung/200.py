class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]  # land 방문 체크 배열
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        island = 0

        def dfs(i, j):
            for k in range(4):
                new_i = i + dx[k]
                new_j = j + dy[k]
                # 아직 방문하지 않았고, 현재와 연결된 land인 경우
                # -> 하나의 섬으로 이어져 있는 경우임
                if 0<=new_i<m and 0<=new_j<n and not visited[new_i][new_j] and grid[new_i][new_j]=='1':
                    visited[new_i][new_j] = 1
                    dfs(new_i, new_j)  # 내 상하좌우로 연결된 land가 있는지 탐색


        for i in range(m):
            for j in range(n):
                # 아직 방문하지 않은 land이면 섬 검사
                if grid[i][j]=='1' and not visited[i][j]:
                    visited[i][j] == 1
                    dfs(i, j)
                    island += 1
        
        return island