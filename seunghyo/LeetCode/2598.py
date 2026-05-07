# Smallest Missing Non-negative Integer After Operations
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        count = {i: 0 for i in range(value)}

        for num in nums:
            if num > 0:
                count[num % value] = count[num % value] + 1
            else:
                divide = -num // value
                last = -num % value
                if last > 0:
                    count[num + value * (divide + 1)] = count[num + value * (divide + 1)] + 1
                else:
                    count[0] = count[0] + 1
        
        current_num = 0 
        while count[0] > 0 and current_num % value == 0:
            for c in count:
                if current_num % value == c and count[c] > 0:
                    count[c] = count[c] - 1
                    current_num += 1
                else:
                    break 

        return current_num
        

