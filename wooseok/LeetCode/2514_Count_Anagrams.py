from collections import Counter

class Solution:
    def countAnagrams(self, s: str) -> int:
        """
        수학문제

        단어단위로 split 후 anagrams 계산해서 곱해주기
        n! // (c1! * c2! * ... * ck!)
        n: 단어 전체 길이
        c: 각 문자의 개수
        """
        MOD = int(1e9) + 7
        res = 1
        for word in s.split():
            n = len(word)
            chars = Counter(word)

            for i in range(1, n + 1):
                res = res * i % MOD
            
            for c in chars.values():
                cnt_fact = 1
                for i in range(1, c + 1):
                    cnt_fact = cnt_fact * i % MOD
                res = res * pow(cnt_fact, -1, MOD) % MOD
        
        return res
