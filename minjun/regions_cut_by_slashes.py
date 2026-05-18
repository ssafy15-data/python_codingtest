class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        visited = []

        for line in grid:
            visited_line = []
            for char in line:
                if char == "/" or char == "\\":
                    visited_line.append([False, False])
                else:
                    visited_line.append(False)
            visited.append(visited_line)

        dxy = [(-1,0), (1,0), (0, -1), (0, 1)]
        dirs = {
            " ": {
                -1: [0, 1, 2, 3]
            },
            "/": {
                0: [0, 2],
                1: [1, 3]
            },
            "\\": {
                0: [1, 2],
                1: [0, 3]
            }
        }
        lrs = {
            " ": {0: -1, 1: -1, 2: -1, 3: -1},
            "/": {0: 1, 1: 0, 2: 1, 3: 0},
            "\\": {0: 0, 1: 1, 2: 1, 3: 0}
        }

        def find_region(r, c, lr=-1):
            stack = [(r,c,lr)]

            while stack:
                x, y, z = stack.pop() # z: 칸 세부위치 (왼쪽 혹은 오른쪽 혹은 해당없음)
                cell = grid[x][y] # 문자
                for dir in dirs[cell][z]: # 진행 가능 방향
                    dx, dy = dxy[dir]
                    n_x = x + dx
                    n_y = y + dy
                    if 0 <= n_x < n and  0 <= n_y < n:
                        n_cell = grid[n_x][n_y] # 칸의 문자
                        n_z = lrs[n_cell][dir] # 진행 방향으로부터 결정되는 세부위치
                        if n_z == -1:
                            if not visited[n_x][n_y]:
                                stack.append((n_x, n_y, n_z))
                                visited[n_x][n_y] = True
                        else:
                            if not visited[n_x][n_y][n_z]:
                                stack.append((n_x, n_y, n_z))
                                visited[n_x][n_y][n_z] = True
            return

        answer = 0
        for r, line in enumerate(visited):
            for c, cell in enumerate(line):
                if cell == True:
                    continue
                elif cell == False:
                    visited[r][c] = True
                    find_region(r, c)
                    answer += 1
                else:
                    if cell[0] == False:
                        cell[0] = True
                        find_region(r, c, 0)
                        answer += 1
                    if cell[1] == False:
                        cell[1] = True
                        find_region(r, c, 1)
                        answer += 1
        return answer


"""
읽어서, matrix로 정의
/ 나 \\가 있는 경우 [0, 0] 으로 저장 (부분적 3차원 배열이 됨)

모든 칸을 돌면서,
섬찾기 처럼, visited 배열을 모두 True 만들면 끝
/에서 왼쪽 칸에 대해선 왼쪽, 위로, 오른쪽 칸에 대해선 오른쪽, 아래로 탐색
\\에서 왼쪽 칸에 대해선 왼쪽, 아래로, 오른쪽 칸에 대해선 오른쪽, 위로 탐색

시간복잡도: O(N^2)
공간복잡도: O(2 * N^2)
"""