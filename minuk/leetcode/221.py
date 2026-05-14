class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        res = 0
        for x in range(1, M + 1):
            for y in range(1, N + 1):
                if (matrix[x - 1][y - 1] == '1'):
                    dp[x][y] = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1
                    res = max(res, dp[x][y])
        return res * res