class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m=len(matrix),len(matrix[0])
        max_sq=[[0]*m for _ in range(n)]

        for r in range(n):
            max_sq[r][0]=int(matrix[r][0]=='1')
        for c in range(m):
            max_sq[0][c]=int(matrix[0][c]=='1')

        for r in range(1,n):
            for c in range(1,m):
                if matrix[r][c]=='0': continue
                max_sq[r][c]=min(max_sq[r-1][c-1],max_sq[r][c-1], max_sq[r-1][c])+1

        return max(max(m) for m in max_sq)**2