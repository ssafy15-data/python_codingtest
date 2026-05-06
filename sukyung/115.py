# Distinct Subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t  = len(s), len(t)
        dp = [[0] * (len_s+1) for _ in range(len_t+1)]  # 행:t, 열:s
        # dp[i][j]: s의 j번째까지의 문자열 사용해서 t의 i번째까지의 문자열 만드는 경우의 수

        # t가 빈 문자열이면 아무것도 안 뽑으므로 s값 상관없이 경우의 수 1
        for j in range(len_s+1):
            dp[0][j] = 1

        for i in range(1, len_t+1):
            for j in range(1, len_s+1):
                if t[i-1] == s[j-1]:  # 실제 문자열 인덱스는 i,j에서 1씩 빼 줘야 함
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                    # dp[i-1][j-1]: s의 전 문자열로 t의 전 문자열을 만든 경우의 수
                    # dp[i][j-1]: 현재 s의 문자를 사용하지 않고, s의 전 문자열로 t를 만든 경우의 수
                    # -> 현재 s의 문자를 사용하는 경우와 사용하지 않는 경우의 합
                else:
                    # 문자가 일치하지 않으므로, 현재 s 문자를 사용하지 않는 경우의 수
                    dp[i][j] = dp[i][j-1]

        return dp[len_t][len_s]