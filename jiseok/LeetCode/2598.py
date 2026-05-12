from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # 우선 0 이상의 정수로 압축
        for i in range(len(nums)):
            nums[i] %= value
        # Counter 사용하여 각 정수의 개수 세기
        nums_counter = Counter(nums)
        # 나올 수 있는 최대 MEX는 len(nums)
        for val in range(len(nums) + 1):
            # value로 나눈 나머지의 개수가 0개면 그 때의 val이 최대 MEX
            # 개수가 남아 있으면 줄여주고 val 증가
            if nums_counter[val % value]:
                nums_counter[val % value] -= 1
            else:
                return val