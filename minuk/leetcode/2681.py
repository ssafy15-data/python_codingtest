class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        nums.sort()
        
        power_sum = 0
        min_sum = 0

        for num in nums:
            power_sum = (power_sum + (((num * num) % MOD) * (num + min_sum))) % MOD
        
            # 현재 값을 포함하는 경우, 포함하지 않는 경우 총 2가지가 발생하여 min_sum은 *2
            min_sum = ((min_sum << 1) + num) % MOD
        
        return power_sum