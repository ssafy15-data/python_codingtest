class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # 부분집합 개수-> 
        # 1차-> 조합 때려서 구하기-> 당연히 시간 초과겠지
        # 2차-> 일단 정렬하고 어쩌지
        # 앞에서부터 가면서 내가 max일 때 이전 애들부터 나까지가 min 후보군
        # 내가 max이자 min이면 3제곱 더해주면 된다
        N = len(nums)
        MOD = int(1e9 + 7)

        nums.sort()
        res = 0

        # min_sum-> max^2 * min공식에서 max가 고정일 때 곱해지는 min의 합
        min_sum = nums[0]
        for i in range(1, N):
            res += nums[i] ** 2 * min_sum
            min_sum = min_sum * 2 + nums[i]
            min_sum %= MOD
            res %= MOD
        # 마지막에 자기가 max이자 min인 경우 추가
        for num in nums:
            res += pow(num, 3, MOD)

        res %= MOD

        return res