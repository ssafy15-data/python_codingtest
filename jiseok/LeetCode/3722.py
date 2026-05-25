class Solution:
    def lexSmallest(self, s: str) -> str:
        result = s
        N = len(s)
        for k in range(1, N + 1):
            s_head = s[:k][::-1] + s[k:]
            s_tail = s[:N - k] + s[N - k:][::-1]
            result = min(result, s_head, s_tail)
        return result