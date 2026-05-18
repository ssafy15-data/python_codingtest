class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        INF = -float('inf')
        n = len(nums)
        tmp = [0] * n
        for idx in range(n):
            if idx and nums[idx] > nums[idx - 1]:
                tmp[idx] = max(tmp[idx - 1], 0) + nums[idx]
            else:
                tmp[idx] = nums[idx]
        end = [INF] * n
        for idx in range(1, n):
            if nums[idx] > nums[idx - 1]:
                end[idx] = nums[idx] + tmp[idx - 1]

        for idx in range(n - 1, -1, -1):
            if idx < n - 1 and nums[idx] < nums[idx + 1]:
                tmp[idx] = max(tmp[idx + 1], 0) + nums[idx]
            else:
                tmp[idx] = nums[idx]
        start = [INF] * n
        for idx in range(n - 1):
            if nums[idx] < nums[idx + 1]:
                start[idx] = nums[idx] + tmp[idx + 1]

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        ans = INF
        max_p = INF

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                p = i - 1
                max_p = max(max_p, end[p] - prefix_sum[p])

                ans = max(ans, max_p + prefix_sum[i - 1] + start[i])
            else:
                max_p = INF
        return ans