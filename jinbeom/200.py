class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        visit=[[False]*n for _ in range(m)]
        ret=0
        for r in range(m):
            for c in range(n):
                if visit[r][c] or grid[r][c]=='0': continue
                ret+=1
                q=[(r,c)]
                visit[r][c]=True
                while q:
                    x,y=q.pop()
                    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                        if 0<=x+dx<m and 0<=y+dy<n and not visit[x+dx][y+dy] and grid[x+dx][y+dy]=='1':
                            q.append((x+dx,y+dy))
                            visit[x+dx][y+dy]=True
        return ret