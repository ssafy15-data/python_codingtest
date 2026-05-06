# Subdomain Visit Count

from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        pair_dict = defaultdict(int)   # key=domain, value=횟수

        for cpdomain in cpdomains:
            rep, domain = cpdomain.split(' ')  # 공백 기준으로 횟수, domain 분할
            pair_dict[domain] += int(rep)
            while '.' in domain:  # subdomain이 있는 동안 반복
                domain = domain.split('.', 1)[1]  # split()[1]-> '.' 기준 상위 domain
                pair_dict[domain] += int(rep)

        res = []
        for k, v in pair_dict.items():
            res.append(f"{v} {k}")

        return res