class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        b_i -> a_i 그래프 연결
        사이클 체크 -> dfs
        """

        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        visit = [0] * numCourses  # 0: 미방문, 1: 방문중, 2: 방문완료

        for i in range(numCourses):
            if visit[i]:
                continue
            stack = [i]
            while stack:
                cur = stack[-1]

                if visit[cur] == 0:
                    visit[cur] = 1

                    for nxt in graph[cur]:
                        if visit[nxt] == 1:  # 순회 중 이미 방문한 노드 접근
                            return False
                        if visit[nxt] == 0:
                            stack.append(nxt)
                elif visit[cur] == 1:  # 순회 완료
                    visit[cur] = 2  # 완료 처리 후 스택에서 제거
                    stack.pop()
                else:  # 이미 방문한 노드
                    stack.pop()

        return True
