class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = {}
        for cpdomain in cpdomains:
            num, full_domain = cpdomain.split(" ")
            num = int(num)
            domains_splitted = list(map(str, full_domain.split(".")))
            len_domains = len(domains_splitted)
            for i in range(len_domains):
                domain = ".".join(domains_splitted[i:len_domains])
                if domain_counts.get(domain):
                    domain_counts[domain] += num
                else:
                    domain_counts[domain] = num

        domains = []
        for domain, num in domain_counts.items():
            domains.append(" ".join([str(num), domain]))

        return domains