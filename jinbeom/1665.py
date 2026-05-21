class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        ret, cur = 0, 0

        for a, m in tasks:
            ret = max(ret, cur + m)
            cur += a

        return ret