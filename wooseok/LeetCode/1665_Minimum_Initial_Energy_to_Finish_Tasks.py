class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        남는 에너지가 많은 것부터 처리 -> 남는 에너지가 많을 수록 다음 작업에 참가하기 더 쉬워짐
        태스크 시작 전 들어갈 수 없다면 에너지 추가
        """
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        cur = 0
        res = 0

        for actual, minimum in tasks:
            if cur < minimum:
                need = minimum - cur
                cur += need
                res += need
            
            cur -= actual
        
        return res
