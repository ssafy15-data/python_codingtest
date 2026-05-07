class Solution:
    def countAnagrams(self, s: str) -> int:
        s_list = s.split()
        MOD = 10 ** 9 + 7

        fact = [1] * (len(s) + 1)
        for i in range(2, len(s) + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        dividend = 1
        divisor = 1

        for word in s_list:
            dividend *= (fact[len(word)] % MOD)
            dict_word = dict()
            for char in word:
                dict_word[char] = dict_word.get(char, 0) + 1
            
            for num in dict_word.values():
                divisor *= (fact[num] % MOD)

        res = (dividend * pow(divisor, -1, MOD)) % MOD
        return res