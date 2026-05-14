# Maximal Square - Medium

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp 해결법
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        # dp[i][j] = (i,j) 까지의 정사각형 한 변의 길이
        
        max_len = 0

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] > max_len:
                max_len = dp[0][j]
        if m >= 2:
            dp[1][0] = int(matrix[1][0])
            if dp[1][0] > max_len:
                max_len = dp[1][0]

        for i in range(1, m):
            for j in range(n):
                if i == 1 and j == 0: continue

                # 0이면 사각형에 추가하지 않으므로 검사 X
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
        
        return max_len ** 2