from collections import Counter

class Solution:
    def countAnagrams(self, s: str) -> int:
        factorial=[1]*(len(s)+1)
        rev_factorial=[1]*(len(s)+1)
        mod=10**9+7

        for i in range(len(s)):
            factorial[i+1]=factorial[i]*(i+1)%mod
        rev_factorial[-1]=pow(factorial[-1],mod-2,mod)
        for i in range(len(s)-1,0,-1):
            rev_factorial[i]=rev_factorial[i+1]*(i+1)%mod

        print(factorial)
        print(rev_factorial)
        ret=1
        for x in s.split():
            n=len(x)
            cnt=Counter(x)
            ret=ret*factorial[n]%mod
            for k in cnt.values():
                ret=ret*rev_factorial[k]%mod
        return ret