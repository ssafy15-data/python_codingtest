class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # 그냥 조건에 맞게 단계별 에너지는 minimum보다 크거나 같게 해서 푸는 문제 같은데
        energy = 0
        tasks.sort(key=lambda x:(x[1] - x[0]), reverse=True)
        for i in range(len(tasks) - 1, -1, -1):
            actual, minimum = tasks[i]
            energy += actual
            if energy < minimum:
                energy = minimum

        return energy
