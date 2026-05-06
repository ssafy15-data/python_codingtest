class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        res_dict = {i:set() for i in range(n)}

        for num1, num2 in restrictions:
            res_dict[num1].add(num2)
            res_dict[num2].add(num1)

        parents = {i:i for i in range(n)}

        def find_parent(num):
            p = parents[num]
            if p == num:
                return num
            else:
                parents[num] = find_parent(p)
                return parents[num]

        def join_parent(num1, num2):
            p1 = find_parent(num1)
            p2 = find_parent(num2)

            if p1 == p2:
                return
            if p1 < p2:
                parents[p2] = p1
                res_dict[p1] |= res_dict[p2]
                res_dict[p1] = set([find_parent(num) for num in res_dict[p1]])
            elif p2 < p1:
                parents[p1] = p2
                res_dict[p2] |= res_dict[p1]
                res_dict[p2] = set([find_parent(num) for num in res_dict[p2]])
            return
                
        output = []
        for num1, num2 in requests:
            p1 = find_parent(num1)
            p2 = find_parent(num2)
            if not (p2 in res_dict[p1] or p1 in res_dict[p2]):
                output.append(True)
                join_parent(p1, p2)
            else:
                output.append(False)

        return output
    

"""
서로소 집합 활용
parent 등록 시 마다, 자식의 restriction 정보를 parent의 restriction에 추가
- 이 때 restriction을 모두 parent로 변환하는 과정 필요
두 집합을 합치려는 시도에서 각 parent의 restriction 정보를 확인
- 두 restriction을 각각 확인해야 함
    - num1을 parent1에 합치는 과정에서 parent1을 num1의 restriction 상대들을 알게되지만,
      num1의 restriction 상대들은 아직 parent1을 알지 못하는 상태이기 때문

시간복잡도: O(N^2)
공간복잡도: O(N^2)
"""