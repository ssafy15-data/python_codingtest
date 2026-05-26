from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # A-Z까지의 카운트 세고 뭘 해야 할까
        # counter 사용해도 될 듯?
        counter = Counter(tasks)
        # 처음에 일단 max개를 배치
        # 그럼 block은 max - 1
        # 총 공간은 (n + 1) * (max - 1) + 1이 나옴
        # 총 공간은 +1이 아니라 max값이 같은 개수 만큼을 더해야 할 듯?
        max_val = max(counter.values())
        max_cnt = 0
        for cnt in counter.values():
            if cnt == max_val:
                max_cnt += 1

        # 총 공간-> max_val이 같은 애들은 묶어서 배치한 상황
        batch_len = (n + 1) * (max_val - 1) + max_cnt
        # 총 공간에 task가 다 못 들어가면 그냥 idle 넣으면 되는거고
        # task가 총 공간보다 넘친다? 그럼 각 block에서 interval에 맞게 알아서 끼어 넣으면 된다-> len(tasks)가 답이 된다
        batch_len = max(batch_len, len(tasks))
        return batch_len