class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # 세로 길이
        n = len(grid[0]) # 가로 길이
        count = 0

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def bfs(x, y):
            queue = []
            queue.append((x, y))
            grid[y][x] = "0"

            while queue:
                cur = queue.pop(0)
                for d in range(4):
                    nx = cur[0] + dx[d]
                    ny = cur[1] + dy[d]

                    if n > nx >= 0 and m > ny >= 0 and grid[ny][nx] == "1":
                        queue.append((nx, ny))
                        grid[ny][nx] = "0"
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(j, i)

        return count




        