class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = [[] for _ in range(n + 1)]
        reverse_edges = [[] for _ in range(n + 1)]
        for a, b in connections:
            edges[b].append(a)
            reverse_edges[a].append(b)
        
        ans = 0
        q = [0]
        visited = [0 for i in range(n + 1)]
        visited[0] = 1
        while q:
            node = q.pop()
            for idx in edges[node]:
                if (not visited[idx]):
                    visited[idx] = 1
                    q.append(idx)
            for idx in reverse_edges[node]:
                if (not visited[idx]):
                    visited[idx] = 1
                    q.append(idx)
                    ans += 1

        return ans