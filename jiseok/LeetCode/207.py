from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # a,b 중에 b가 선수과목
        # 진입차수랑 인접 리스트 만들기
        in_degree = [0 for _ in range(numCourses)]
        adj_list = {v: [] for v in range(numCourses)}

        for a, b in prerequisites:
            in_degree[a] += 1
            adj_list[b].append(a)
        
        queue = deque()
        for sub in range(numCourses):
            if in_degree[sub] == 0:
                queue.append(sub)
        
        while queue:
            sub = queue.popleft()
            for next_sub in adj_list[sub]:
                in_degree[next_sub] -= 1
                if in_degree[next_sub] == 0:
                    queue.append(next_sub)
        
        if sum(in_degree) == 0:
            return True
        else:
            return False
