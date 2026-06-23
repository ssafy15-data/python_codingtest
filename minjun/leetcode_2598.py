class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        negatives = [num for num in nums if num < 0]
        plus = [num for num in nums if num >= 0]

        for num in negatives:
            temp_num = -num
            temp_num = temp_num % value
            temp_num = value - temp_num
            plus.append(temp_num)

        changed = [num % value for num in plus]

        nums_dict = {num:0 for num in range(value)}
        for num in changed:
            nums_dict[num] += 1

        if nums_dict[0] == 0:
            return 0

        answer = 0
        min_cnt = 1e9

        for num, cnt in nums_dict.items():
            if cnt == 0:
                answer = num
                break
            if cnt < min_cnt:
                min_cnt = cnt
                answer = value * cnt + num
        
        return answer
