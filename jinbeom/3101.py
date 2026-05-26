class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        ret=1

        for idx in range(n-2,-1,-1):
            dp[idx]=dp[idx+1]+1 if nums[idx]!=nums[idx+1] else 1
            ret+=dp[idx]

        return ret