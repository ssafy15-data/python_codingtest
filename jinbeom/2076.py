class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(u):
            while parent[u] != u:
                u = parent[u]
            return u

        def union(u, v):
            p, q = find(u), find(v)
            if rank[p] < rank[q]:
                parent[p] = q
            elif rank[p] > rank[q]:
                parent[q] = p
            else:
                parent[q] = p
                rank[p] += 1

        ret = []

        for u, v in requests:
            p, q = find(u), find(v)
            if p == q:
                ret.append(True)
                continue
            tmp = True
            for x, y in restrictions:
                if (find(x)==p and find(y)==q) or (find(x)==q and find(y)==p):
                    tmp = False
                    break
            ret.append(tmp)
            if tmp: union(u, v)

        return ret

