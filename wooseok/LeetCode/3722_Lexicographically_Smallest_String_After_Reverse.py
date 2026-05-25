class Solution:
    def lexSmallest(self, s: str) -> str:
        """
        사전순
        a가 최대한 앞쪽으로
        or
        z가 최대한 뒤쪽으로

        n <= 1000
        가능한 경우의 수가 2n
        실제 연산 n^2
        완탐
        """
        n = len(s)
        res = s
        for k in range(1, n + 1):
            front_reversed = s[:k][::-1] + s[k:]
            if front_reversed < res:
                res = front_reversed
            
            back_reversed = s[:k] + s[k:][::-1]
            if back_reversed < res:
                res = back_reversed
            
        return res
