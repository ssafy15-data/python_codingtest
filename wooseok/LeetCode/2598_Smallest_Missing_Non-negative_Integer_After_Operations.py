from collections import Counter

class Solution:
    """
    문제 이해
    더하고 빼고 -> 나머지 연산
    앞에서 부터 채웠을 때 비는 수
    """

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod_nums = Counter()
        for num in nums:
            mod_nums[num % value] += 1
        
        mex = 0
        while True:
            if mod_nums[mex % value] > 0:
                mod_nums[mex % value] -= 1
                mex += 1
            else:
                return mex
