class Solution:
    """
    union find
    find로 조합 체크
    union 후 restrictions -> find root 조합 형태로 갱신
    """
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                if rank[a] < rank[b]:
                    parent[a] = b
                elif rank[a] > rank[b]:
                    parent[b] = a
                else:
                    parent[b] = a
                    rank[a] += 1

        parent = list(range(n))
        rank = [0] * n
        res = []
        for a, b in requests:
            a = find(a)
            b = find(b)
            if a == b:
                res.append(True)
                continue
            a, b = (b, a) if a > b else (a, b)
            for i, (u, v) in enumerate(restrictions):
                u = find(u)
                v = find(v)
                restrictions[i] = [u, v]
                if (a == u and b == v) or (a == v and b == u):
                    res.append(False)
                    break
            else:
                union(a, b)
                res.append(True)
        
        return res
