class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        post_courses = [[] for i in range(numCourses)]
        count = [0 for i in range(numCourses)]
        for a, b in prerequisites:
            post_courses[b].append(a)
            count[a] += 1
        
        q = []
        for i in range(numCourses):
            if (not count[i]):
                q.append(i)
        
        while (q):
            x = q.pop()
            for idx in post_courses[x]:
                count[idx] -= 1
                if (not count[idx]):
                    q.append(idx)
        
        return not any(count)