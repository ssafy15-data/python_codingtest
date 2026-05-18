class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # O(N)이나 O(NlogN)
        # 리스트에다가 지금까지 몇 개의 수가 달랐는가를 저장
        # 그럼 리스트가 의미하는 게 해당 인덱스까지의 가능한 subarray 개수 의미
        # 그냥 count하면 끝?
        N = len(nums)
        # cnt_list = [1 for _ in range(N)]
        # for i in range(1, N):
        #     if nums[i] != nums[i - 1]:
        #         cnt_list[i] = cnt_list[i - 1] + 1

        # return sum(cnt_list)


        # Runtime / Memory 맘에 안 들어서 리스트 안 쓰고 풀이
        ans = 1
        cur_acc = 1
        for i in range(1, N):
            if nums[i] != nums[i - 1]:
                cur_acc += 1
            else:
                cur_acc = 1
            ans += cur_acc

        return ans