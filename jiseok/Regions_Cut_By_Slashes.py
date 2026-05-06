from collections import deque

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        # 3배로 늘려서 영역 표시
        regions = [[0 for _ in range(3 * n)] for _ in range(3 * n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == '/':
                    regions[3 * r][3 * c + 2] = 1
                    regions[3 * r + 1][3 * c + 1] = 1
                    regions[3 * r + 2][3 * c] = 1
                elif grid[r][c] == '\\':
                    regions[3 * r][3 * c ] = 1
                    regions[3 * r + 1][3 * c + 1] = 1
                    regions[3 * r + 2][3 * c + 2] = 1
        
        def search(row, col): # 영역에 대해서 나눠진 부분 구하기
            nonlocal cnt
            drow = [-1, 0, 1, 0] # 상 우 하 좌
            dcol = [0, 1, 0, -1]

            queue = deque([[row, col]])
            regions[row][col] = 1
            while queue:
                row, col = queue.popleft()
                for k in range(4):
                    nrow = row + drow[k]
                    ncol = col + dcol[k]
                    if 0 <= nrow < 3 * n and 0 <= ncol < 3 * n and not regions[nrow][ncol]:
                        queue.append([nrow, ncol])
                        regions[nrow][ncol] = 1
            cnt += 1
            return
        
        cnt = 0
        for r in range(3 * n):
            for c in range(3 * n):
                if regions[r][c] == 0:
                    search(r, c)

        return cnt
