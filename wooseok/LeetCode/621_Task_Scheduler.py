class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        interval을 그룹으로 묶어서
        걍 많은 것부터 순서대로 하면 되는거 아닌가
        """

        from collections import Counter
        cnt = Counter(tasks)
        
        freqs = list(cnt.values())
        max_freq = max(freqs)
        max_freq_cnt = freqs.count(max_freq)

        res = (max_freq - 1) * (n + 1) + max_freq_cnt

        return max(res, len(tasks))
