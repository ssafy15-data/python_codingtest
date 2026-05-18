class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        """
        n <= 10^5 => N^2불가
        
        + -> - -> + 구간은 찾아둬야됨
        그 이후 양 쪽 인덱스 조절하면서 경우의 수를 추려서 비교
        최소 경우만 찾고 양 인덱스를 늘리는 형식으로 변경하며 그 구간의 최댓값만 남기는 형식으로 구하자
        """

        n = len(nums)
        i = 0
        res = -int(1e14)
        while i < n:
            l = i
            i += 1

            while i < n and nums[i - 1] < nums[i]:
                i += 1
            if i == l + 1:  # 상승 없음
                continue
            
            p = i - 1  # 고점
            s = nums[p - 1] + nums[p]  # nums[l] + num[p]의 최소 경우

            while i < n and nums[i - 1] > nums[i]:
                s += nums[i]  # 하락 구간 무조건 더해야 됨
                i += 1

            if i == p + 1 or i == n or nums[i - 1] == nums[i]:  # 하락없음 or 평행
                continue
            
            q = i - 1  # 저점

            if i == n or nums[i - 1] >= nums[i]:  # 저점에서 다시 오르지 않으면 실패
                continue
            
            s += nums[i]  # 다시 오르는 경우 최소한 더해줘야됨
            i += 1

            # 오른쪽 인덱스 확장
            cur, cur_max = 0, 0
            while i < n and nums[i - 1] < nums[i]:
                cur += nums[i]
                cur_max = max(cur, cur_max)
                i += 1
            s += cur_max

            # 왼쪽 인덱스 확장
            cur, cur_max = 0, 0
            for j in range(p - 2, l - 1, -1):
                cur += nums[j]
                cur_max = max(cur, cur_max)
            s += cur_max

            res = max(res, s)
            
            i = q  # +- 스킵 다시 마지막 상승부터 시작
    
        return res
