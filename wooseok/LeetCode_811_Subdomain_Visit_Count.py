from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        
        for cpdomain in cpdomains:
            reps, domain = cpdomain.split()
            reps = int(reps)

            parts = domain.split('.')
            for i in range(len(parts)):
                counts['.'.join(parts[i:])] += reps
        
        return [f"{c} {d}" for d, c in counts.items()]
