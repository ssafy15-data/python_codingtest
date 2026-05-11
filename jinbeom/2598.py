class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        tmp={i:0 for i in range(value)}
        for num in nums:
            tmp[num%value]+=1

        a=min(tmp,key=lambda x:tmp[x])

        return value*tmp[a]+a