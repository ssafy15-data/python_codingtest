from collections import Counter

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7 #나눌 수
        words = s.split()
        max_len = len(s)

        fact = [1] * (max_len + 1)

        for i in range(2, max_len + 1):
            fact[i] = (fact[i-1] * i) % MOD
            
        ans = 1

        for word in words:
            n = len(word)
            word_count = fact[n]
            counts = Counter(word)
            
            denominator = 1
            for char in counts:
                denominator = (denominator * fact[counts[char]]) % MOD
                
            inv_denominator = pow(denominator, MOD - 2, MOD)
            word_anagrams = (word_count * inv_denominator) % MOD

            ans = (ans * word_anagrams) % MOD
            
        return ans