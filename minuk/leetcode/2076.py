class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        def getParent(a):
            if (a != parent[a]): parent[a] = getParent(parent[a])
            return parent[a]
        
        def unionFind(a, b):
            a = getParent(a)
            b = getParent(b)

            if (a != b):
                parent[a] = b
        
        parent = [i for i in range(n + 1)]

        answer = []
        for request in requests:
            a, b = request
            a, b = getParent(a), getParent(b)
            if (a == b):
                answer.append(True)
            else:
                check = 0
                for restriction in restrictions:
                    c, d = restriction
                    c, d = getParent(c), getParent(d)
                    if ((a == c and b == d) or (a == d and c == b)):
                        check = 1
                        answer.append(False)
                        break
                if (not check):
                    unionFind(a, b)
                    answer.append(True)
        return answer