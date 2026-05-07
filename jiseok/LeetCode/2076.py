class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
    # union find로 하는 거 같은데
    # 어케 하지
        result = []
        p = [v for v in range(n)]

        def find_set(x):
            if p[x] != x:
                p[x] = find_set(p[x])
            return p[x]
    
        # rank는 굳이?
        def union_set(x, y):
            root_x = find_set(x)
            root_y = find_set(y)
            if root_x != root_y:
                p[root_y] = root_x
            return

        for u, v in requests:
            root_u = find_set(u)
            root_v = find_set(v)
            can_be_friend = True

            if root_u != root_v:
                # 일단 진짜 union하지는 말고
                # 어떤 경우에 안 되는지 생각
                # 그룹 2개가 합쳐지는데 두 명이 같은 그룹이 되는 경우
                # -> 각 친구가 각 그룹에 존재하는 경우 + 이미 같은 그룹인 경우-> 이미 같은 그룹인 경우는 있을 수 없으니까 패스
                for a, b in restrictions:
                    root_a = find_set(a)
                    root_b = find_set(b)
                    if (root_a == root_u and root_b == root_v) or (root_a == root_v and root_b == root_u):
                        can_be_friend = False
                        break
            # 친구가 될 수 있으면 u랑 v union하고 result append
            # 없으면 그냥 result에만 append 
            if can_be_friend:
                union_set(u, v)
                result.append(True)
            else:
                result.append(False)
        return result