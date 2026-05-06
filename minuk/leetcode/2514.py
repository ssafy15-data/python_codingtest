import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        res = 1
        MOD = int(1e9 + 7)
        std = ord('a')
        for string in s.split():
            value = 1
            alpha = [0 for i in range(27)]
            for i in string:
                alpha[ord(i) - std] += 1
            length = len(string)
            for i in range(26):
                if (alpha[i]):
                    value = (value * math.comb(length, alpha[i])) % MOD
                    length -= alpha[i]
            res = (res * value) % MOD
        return res