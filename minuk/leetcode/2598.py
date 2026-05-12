class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        values = [0 for i in range(value + 1)]
        for num in nums:
            values[num % value] += 1
        min_value = int(1e9)
        min_index = -1
        for i in range(value):
            if (values[i] < min_value):
                min_value = values[i]
                min_index = i
        
        return min_value * value + min_index