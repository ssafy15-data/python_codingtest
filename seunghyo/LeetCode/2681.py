# Power of Heroes
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        MOD = 10**9 + 7
        total = 0
        prefix_sum = 0  

        for max_val in nums:
            total += max_val * max_val * (prefix_sum + max_val)
            #print(max_val,  prefix_sum)
            total %= MOD
            prefix_sum = (prefix_sum * 2 + max_val) % MOD
        
        return total

        