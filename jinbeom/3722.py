class Solution:
    def lexSmallest(self, s: str) -> str:
        ret=s
        for k in range(1,len(s)+1):
            ret = min(ret, s[:k][::-1] + s[k:])
            ret = min(ret, s[:len(s) - k] + s[len(s) - k:][::-1])
        return ret