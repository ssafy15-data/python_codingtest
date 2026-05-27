# Task Scheduler - Medium

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = Counter(tasks)  # 각 task별 개수 dict
        start_time = {k:-(n+1) for k in task_dict.keys()}  # 각 task별 처리된 시간
        interval = 0  # 현재 시간
        task_sum = 0  # 처리된 task 수
        N = len(tasks)

        while task_sum < N:
            max_cnt = 0   # 가장 개수 많이 남은 task 우선 사용하기 위해 비교할 변수
            task = None
            for k, v in task_dict.items():
                if v == 0:  # 처리할 task가 남아있지 않다면 pass
                    continue
                # 현재 시각 - task 처리 시간이 n보다 크거나 같아 실행 가능한 경우만 검사
                # 가장 개수가 많이 남은 task 우선 사용
                if interval-start_time[k]>n and v>=max_cnt:
                    max_cnt = v
                    task = k

            # 가장 개수 많은 task 진행 or 진행할 수 있는 task가 없다면 idle
            if task != None:
                task_dict[task] -= 1
                task_sum += 1
                start_time[task] = interval

            interval += 1
        
        return interval