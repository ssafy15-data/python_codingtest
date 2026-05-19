class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        cnts = []
        prev = nums[0]
        cnt = 1
        for num in nums:
            if num != prev:
                cnt += 1
            else:
                if cnt > 1:
                    cnts.append(cnt)
                    cnt = 1
            prev = num
        
        if cnt > 1:
            cnts.append(cnt)
        
        answer = len(nums)
        for cnt in cnts:
            answer += cnt*(cnt-1)//2
        
        return answer