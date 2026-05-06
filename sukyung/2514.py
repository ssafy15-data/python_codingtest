# Count Anagrams

from collections import Counter
import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        sub_s = s.split(' ')  # 공백 기준 문자열 분리
        ans = 1
        for sub in sub_s:
            dict_sub = Counter(sub)  # 같은 것이 있는 문자의 개수 알기 위해
            denom = 1
            for v in dict_sub.values():
                if v != 1:
                    denom *= math.factorial(v)

            # 같은 것이 있는 순열의 개수 = n! / (p!*q!...)
            len_anagram = math.factorial(len(sub)) // denom
            ans *= len_anagram
            ans = ans % (10**9 + 7)

        return ans