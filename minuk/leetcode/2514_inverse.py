import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = int(1e9 + 7)
        def modularPow(base, exp, mod):
            cnt = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    cnt = (cnt * base) % mod
                base = (base * base) % mod
                exp //= 2
            return cnt

        def modInverse(a, p):
            return modularPow(a, p - 2, p)

        l = len(s)
        factorial = [1 for i in range(l + 1)]
        factorial_inverse = [1 for i in range(l + 1)]

        for i in range(1, l + 1):
            factorial[i] = (factorial[i - 1] * i) % MOD
        
        factorial_inverse[l] = modInverse(factorial[l], MOD)
        for i in range(l - 1, 1, -1):
            factorial_inverse[i] = factorial_inverse[i + 1] * (i + 1) % MOD
        
        res = 1
        std = ord('a')
        for string in s.split():
            alpha = [0 for i in range(27)]
            for i in string:
                alpha[ord(i) - std] += 1
            value = factorial[len(string)]
            for i in range(26):
                if (alpha[i]):
                    value = (value * factorial_inverse[alpha[i]]) % MOD
            res = (res * value) % MOD
        
        return res