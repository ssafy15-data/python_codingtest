class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()

        len_nums = len(nums)
        answer = 0

        # 간격 0
        for num in nums:
            answer += num*num*num
            answer = int(answer % (1e9+7))

        # 간격 1
        for i in range(len_nums-1):
            answer += (nums[i+1]*nums[i+1] * nums[i])
            answer = int(answer % (1e9+7))

        # 간격 2 이상
        factorials = [1]

        def factorial(k):
            if len(factorials) < k:
                for i in range(len(factorials)+1, k+1):
                    factorials.append(factorials[-1]*i)
            return factorials[k-1]

        def cal_comb(n, k):
            k = min(k, n-k)
            if k == 0:
                return 1
            mul_num = 1
            for i in range(k):
                mul_num *= (n-i)
            return mul_num // factorial(k)

        for i in range(2, len_nums):
            sumnum = 1
            for k in range(1, i):
                sumnum += cal_comb(i-1, k)
            for idx in range(len_nums-i):
                answer += sumnum*(nums[idx+i]*nums[idx+i]*nums[idx])
                answer = int(answer % (1e9+7))
        
        return answer
    
# -------------------------------------------------------------------------

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        MOD = 10**9 + 7
        
        answer = 0
        temp_sum = 0
        
        for num in nums:
            answer = (answer + (num * num * (num + temp_sum))) % MOD
            temp_sum = (temp_sum * 2 + num) % MOD
            
        return answer
