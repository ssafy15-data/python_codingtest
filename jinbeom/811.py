from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result=defaultdict(int)
        for cpdomain in cpdomains:
            cnt,domain=cpdomain.split(' ')
            cnt=int(cnt)
            tmp=domain.split('.')
            for idx in range(len(tmp)):
                result[".".join(tmp[idx:])]+=cnt
        ret=[]
        for domain in result:
            ret.append(str(result[domain])+" "+domain)
        return ret
