class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False]*n for _ in range(m)]
        answer = 0

        # dfs로 하나의 섬에 대해 방문 처리 (+주변 바다도 방문처리함)
        dxy = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def find_island(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for dx, dy in dxy:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                        continue
                    if not visited[new_x][new_y] and grid[new_x][new_y] == "1":
                        stack.append((new_x, new_y))
                    visited[new_x][new_y] = True

        # 모든 칸을 순회하면서, 방문하지 않았던 land인 경우 find_island 호출
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    find_island(i, j)
                    answer += 1

        return answer