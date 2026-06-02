# Count Alternating Subarrays - Medium

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        pre = -1
        l = 0  # 현재까지 연속된 subarray 길이
        for num in nums:
            if num != pre:
                # 앞의 값과 다르다면 subarray 길이 + 1
                l += 1
            else:
                # 앞의 값과 동일하면 subarray 초기화이므로 길이 1
                l = 1
                
            ans += l
            pre = num
        
        return ans