# Smallest Missing Non-negative Integer After Operations

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        '''
        nums의 각 num들을 value로 나눈 나머지가 동일하면
        num에 value를 더하거나 빼서 동일한 수로 만들기 가능
        -> 각 나머지 별 개수 센 후, 차례대로 숫자 만들다 더 이상 나머지로 만들 수 없는 숫자가 정답
        '''
        # key: value로 나눠 나올 수 있는 나머지, value: num%value=key의 개수
        nums_mod = {k:0 for k in range(value)}
        for num in nums:
            k = num % value
            nums_mod[k] += 1
        
        ans, count = 0, nums_mod[0]
        for mod, cnt in nums_mod.items():
            # 나머지 개수(cnt)가 count보다 작다면 해당 나머지가 부족할 것
            if cnt < count:
                ans, count = mod, cnt
                # cnt==0이면 해당 mod로 만들 수 있는 숫자가 아예 없다는 뜻이므로 더 이상 검사할 필요 X
                if not cnt:
                    break
        
        return count*value+ans