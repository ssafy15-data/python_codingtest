#Task Scheduler
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = Counter(tasks)
        frequencies = list(task_counts.values())
        max_freq = max(frequencies)

        max_freq_count = frequencies.count(max_freq)

        ans = (max_freq - 1) * (n + 1) + max_freq_count
        
        return max(ans, len(tasks))