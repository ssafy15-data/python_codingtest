from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt=Counter(tasks)
        tmp, max_val=0,0
        for k in cnt.values():
            if k>max_val: max_val,tmp=k,1
            elif k==max_val: tmp+=1
        return max((max_val-1)*(n+1)+tmp, len(tasks))