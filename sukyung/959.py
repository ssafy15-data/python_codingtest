# Regions Cut By Slashes

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # 선이 그어져 생기는 공간을 탐색하기 위해 3*3 크기로 확대
        arr = [[0] * (n*3) for _ in range(n*3)]
        # 슬래시 부분 1로 변경
        for i in range(n):
            p = 3 * i
            for j in range(n):
                q = 3 * j
                if grid[i][j] == '/':
                    arr[p][q+2] = arr[p+1][q+1] = arr[p+2][q] = 1
                elif grid[i][j] == '\\':
                    arr[p][q] = arr[p+1][q+1] = arr[p+2][q+2] = 1
        
        # 도형(선 사이 공간) 개수 세기
        ans = 0
        for i in range(n*3):
            for j in range(n*3):
                # arr에서 선이 아닌 공간인 경우
                if not arr[i][j]:
                    ans += 1  # 도형 개수 1 증가
                    arr[i][j] = 1
                    st = [(i, j)]  # stack 생성
                    # dfs 탐색
                    while st:
                        di, dj = st.pop()
                        for r, c in [(1,0), (-1,0), (0,1), (0,-1)]:
                            dr, dc = di+r, dj+c
                            if 0<=dr<n*3 and 0<=dc<n*3 and not arr[dr][dc]:
                                arr[dr][dc] = 1
                                st.append((dr, dc))

        return ans