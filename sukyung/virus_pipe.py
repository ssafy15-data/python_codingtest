from collections import deque
from collections import defaultdict

def solution(n, infection, edges, k):
    answer = 0
    graph = defaultdict(list)
    for x, y, type in edges:
        graph[x].append((y, type))
        graph[y].append((x, type))
    
    infected = [0] * (n+1)  # 감염 여부 나타내는 list
    infected[infection] = 1
    cur_infected = [infection]  # 현재까지 감염된 배양체 번호 저장
    
    def dfs(i, last_type):
        nonlocal answer
        if i == k:
            answer = max(answer, len(cur_infected))
            return
        for type in range(1, 4):
            # 직전에 열었던 파이프인 경우, 다른 파이프를 열도록 pass
            if type == last_type: continue
            
            # 인접한 배양체 감염 처리
            new_infected = []  # type 파이프를 통해 새로 감염될 배양체 배열
            q = deque(cur_infected)  # 연결된 배양체 탐색할 큐
            while q:
                node = q.popleft()
                for next, t in graph[node]:  # 인접한 배양체 탐색
                    # 아직 감염되지 않았고, 파이프 종류가 같은 경우
                    if not infected[next] and t==type:
                        infected[next] = 1  # 감염 처리
                        cur_infected.append(next)
                        new_infected.append(next)
                        q.append(next)
                        
            dfs(i+1, type)
            
            # 감염 처리 되돌리기
            for node in new_infected:
                infected[node] = 0
                cur_infected.pop()
                        
    dfs(0, -1)
    
    return answer