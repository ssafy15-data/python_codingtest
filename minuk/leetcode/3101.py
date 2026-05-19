class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        res = 1
        count = 1
        for i in range(1, N):
            if (nums[i] == nums[i - 1]):
                count = 1
            else:
                count += 1
            res += count
        
        return res