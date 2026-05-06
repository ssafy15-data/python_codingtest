# Regions cut by slashes
from collections import deque
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        table = [[0 for _ in range(n * 3)] for _ in range(n * 3)]

    
        for g in range(n):
            arr = list(grid[g])

            for idx in range(n):
                if arr[idx] == "\\":
                    table[g * 3][idx * 3] = 1
                    table[g * 3 + 1][idx * 3 + 1] = 1
                    table[g * 3 + 2][idx * 3 + 2] = 1
                elif arr[idx] == "/":
                    table[g * 3][idx * 3 + 2] = 1
                    table[g * 3 + 1][idx * 3 + 1] = 1
                    table[g * 3 + 2][idx * 3] = 1

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            table[x][y] = 1

            while queue:
                curX, curY = queue.popleft()
                for d in range(4):
                    nx = curX + dx[d]
                    ny = curY + dy[d]
                    if n * 3 > nx >= 0 and n * 3 > ny >= 0 and table[nx][ny] == 0:
                        queue.append((nx, ny))
                        table[nx][ny] = 1

        area = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if table[i][j] == 0:
                    area += 1
                    bfs(i, j)

        return area

        