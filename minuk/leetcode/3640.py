class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        N = len(nums)
        MIN_VALUE = -int(1e16)
        res = dp0 = dp1 = dp2 = MIN_VALUE
        
        for i in range(1, N):
            if (nums[i] > nums[i - 1]): 
                new_dp2 = max(dp2 + nums[i], dp1 + nums[i])
                new_dp0 = max(dp0 + nums[i], nums[i - 1] + nums[i])
                
                dp0 = new_dp0
                dp1 = MIN_VALUE
                dp2 = new_dp2
            
            elif (nums[i] < nums[i - 1]):
                new_dp1 = max(dp1 + nums[i], dp0 + nums[i])
                
                dp0 = MIN_VALUE
                dp1 = new_dp1
                dp2 = MIN_VALUE
            
            else:
                dp0 = dp1 = dp2 = MIN_VALUE
            
            res = max(res, dp2)
        
        return res