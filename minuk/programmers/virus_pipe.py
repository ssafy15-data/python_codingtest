def solution(n, infection, edges, k):
    answer = 0
    combinations = []
    stack = [[]]
    while (stack):
        temp_list = stack.pop()
        if (len(temp_list) == k):
            combinations.append(temp_list)
            continue
        for i in range(1, 4):
            if (temp_list and temp_list[-1] == i): continue
            stack.append(temp_list + [i])
    
    adj_edges = [[[], [], [], []] for i in range(n + 1)]
    for edge in edges:
        a, b, c = edge
        adj_edges[a][c].append(b)
        adj_edges[b][c].append(a)
        
    res = 0
    for comb in combinations:
        visited = [0 for i in range(n + 1)]
        count = 0
        state = [adj_edge[:] for adj_edge in adj_edges[infection]]
        for now_pipe in comb:
            while (state[now_pipe]):
                now_state = state[now_pipe].pop()
                if (visited[now_state]): continue
                visited[now_state] = 1
                count += 1
                for i in range(4):
                    state[i].extend(adj_edges[now_state][i])
        res = max(res, count)
    
    return res