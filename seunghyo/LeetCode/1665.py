#Minimum Initial Energy to Finish Tasks
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: -(x[1]-x[0]))
        init = tasks[0][1] # 초기 값
        
        current = init
        for task in tasks:
            cost = task[0]
            need = task[1]

            if current >= need:
                current -= cost
            else:
                gap = need - current
                init += gap
                current = need - cost
        
        return init
