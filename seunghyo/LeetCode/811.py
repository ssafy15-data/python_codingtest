class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)

            subdomains = domain.split(".")

            for i in range(len(subdomains)):
                sub = ".".join(subdomains[i:])
                counts[sub] = counts.get(sub, 0) + count

        return [f"{v} {k}" for k, v in counts.items()]
