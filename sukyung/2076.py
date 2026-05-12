# Process Restricted Friend Requests

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:       
        root = [i for i in range(n)]

        def find_root(n):
            root_n = root[n]
            if root_n == n:
                return n
            root[n] = find_root(root_n)
            return root[n]

        ans = []
        for x, y in requests:
            r_x, r_y = find_root(x), find_root(y)
            if r_x == r_y:  # 이미 간접/직접적으로 친구가 되어 있는 경우 -> 전에 검사했을 것이므로, 친구가 되어도 괜찮다는 뜻
                ans.append(True)
                continue

            flag = True    
            for a, b in restrictions:
                r_a, r_b = find_root(a), find_root(b)
                # 친구가 되면 안 되는 애들이 x, y의 그룹에 속해 있는 경우
                # -> x, y가 union되면 안 됨 -> false
                if (r_x==r_a and r_y==r_b) or (r_x==r_b and r_y==r_a):
                    flag = False
                    break

            if flag:
                ans.append(True)
                root[r_y] = r_x  # y 그룹과 x 그룹 union
            else:
                ans.append(False)
            
        return ans