class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        DP
        1인 인덱스만 체크
        i, j => 오른쪽 아래 인덱스. 한 변 길이
        """
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        max_val = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_val = max(max_val, dp[i][j])

        return max_val * max_val
