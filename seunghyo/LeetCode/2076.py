# Process Restricted Friend Requests
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        answer = []

        for u,v in requests:
            ru, rv = find(u), find(v)
        
            blocked = False
            for x, y in restrictions:
                rx, ry = find(x), find(y)
                if (ru == rx and rv == ry) or (ru == ry and rv == rx):
                    blocked = True
                    break
            if blocked:
                answer.append(False)
            else:
                answer.append(True)
                if ru != rv:
                    parent[ru] = rv
        
        return answer
