class Solution:
    def countAnagrams(self, s: str) -> int:
        
        MOD = 10**9 + 7
        s_li = s.split(" ")

        max_len = max([len(word) for word in s_li])
        factorials = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            factorials[i] = (factorials[i-1] * i) % MOD
        
        answer = 1
        for word in s_li:
            word_count = {}
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1

            full_cnt = factorials[len(word)]
            denominator = 1
            for char, cnt in word_count.items():
                if cnt > 1:
                    denominator = (denominator * factorials[cnt]) % MOD
            val = (full_cnt * pow(denominator, MOD-2, MOD)) % MOD
            answer = (answer * val) % MOD

        return answer