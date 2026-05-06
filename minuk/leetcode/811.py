class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = dict()
        for cpdomain in cpdomains:
            rep, domain = cpdomain.split()
            rep = int(rep)
            domain = domain.split('.')
            for i in range(len(domain)):
                subdomain = '.'.join(domain[i:])
                if (subdomain not in domains):
                    domains[subdomain] = 0
                domains[subdomain] += rep
        res = []
        for key, value in domains.items():
            res.append(f"{value} {key}")
        return res