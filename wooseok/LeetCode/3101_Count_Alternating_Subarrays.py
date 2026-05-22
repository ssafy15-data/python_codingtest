class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        """
        alternating array가 만들어지기 전까지 순차적으로 계속 증가함
        끊길 때 그 만큼 누적된 값을 더해주면 됨
        """
        acc = 0
        n = len(nums)
        acc = 1
        res = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                acc += 1
            else:
                acc = 1
            res += acc
        return res
