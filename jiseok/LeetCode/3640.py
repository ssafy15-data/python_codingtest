class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # dp 문제 같은데
        N = len(nums)
        in_or_decrease = [0 for _ in range(N)] # 현재 인덱스 기준에서 다음이 감소면 -1, 증가면 1, 그대로면 0
        for i in range(N - 1):
            if nums[i] > nums[i + 1]:
                in_or_decrease[i] = -1
            elif nums[i] < nums[i + 1]:
                in_or_decrease[i] = 1

        # 0이 나오면 무조건 처음부터 
        # 시작 인덱스 기억해야할 듯
        # 현재 상태도 저장-> 증가 중(첫 번째)인지 감소 중인지 증가 중(두 번째)인지
        cur_state = 0
        start_idx = -1
        dp = [float('-inf') for _ in range(N)]
        for i in range(N - 1):
            if cur_state == 0:
                # 지금까지의 상태가 유지일 때 다음이 증가한다면 상태는 1로 변경하고 시작 인덱스 설정
                if in_or_decrease[i] == 1:
                    cur_state = 1
                    start_idx = i

            # 지금까지의 상태가 증가 중(첫 번째)일 때
            elif cur_state == 1:
                # 다음이 감소라면
                if in_or_decrease[i] == -1:
                    cur_state = 2
                elif in_or_decrease[i] == 0:
                    cur_state = 0

            # 지금까지의 상태가 감소 중일 때
            elif cur_state == 2:
                if in_or_decrease[i] == 1:
                    cur_state = 3
                    # 오답의 이유가 second_start_idx 같은데 어떻게 처리해야 할지 모르겠음
                    second_start_idx = i
                elif in_or_decrease[i] == 0:
                    cur_state = 0

            # 지금까지의 상태가 증가 중(두 번째)일 때
            else:
                if in_or_decrease[i] == -1:
                    cur_state = 2
                    start_idx = second_start_idx
                elif in_or_decrease[i] == 0:
                    cur_state = 0
            
            if cur_state == 3:
                dp[i] = sum(nums[start_idx : i + 2])

        return max(dp)
